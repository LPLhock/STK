#coding=utf-8

import os
import requests
import math
import numpy as np
import pandas as pd
import baostock as bs
import jqdatasdk as jq
import time

from datetime import datetime,timedelta
from multiprocessing import Pool
from functools import partial
from tqdm import tqdm


class BaosAgent:
    
    path_src = './data/'
    
    def __init__(self, sto_ids):
        self.all_sids = sto_ids

    @staticmethod
    def complement_exist_data_proc(sub_file_sto_ids, freq):
        bs.login()
        fn_path = BaosAgent.path_src + str(freq) + os.sep
        for sto_id in tqdm(sub_file_sto_ids):
            file_df = BaosAgent.read_freq_df(freq, sto_id)
            if freq == 240:
                start_date = datetime.strftime(datetime.now() - timedelta(days=10), '%Y-%m-%d')
                new_df = BaosAgent.get_freq_data_from_bs(sto_id, start_date, freq)
                new_df.code = new_df.code.str[3:]
                new_df = new_df[new_df.tradestatus == '1']
                new_df = new_df.reset_index(drop=True)
                
                new_df[['open', 'high', 'low', 'close', 'volume', 'turn']] = new_df[['open', 'high', 'low', 'close', 'volume', 'turn']].astype(float)

                exist_dates = file_df.date.values
                exist_new_data = False
                for idx in new_df.index:
                    daily_data = new_df.iloc[idx]
                    if (daily_data.date not in exist_dates) and (daily_data.tradestatus == '1'):
                        file_df = file_df.append(daily_data, ignore_index=True)
                        exist_new_data = True
                if exist_new_data:
                    fn = fn_path + sto_id + '.pkl'
                    file_df.to_pickle(fn, compression='xz')
    
    @staticmethod
    def complement_exist_data(freq):
        bs.login()
        fn_path = BaosAgent.path_src + str(freq) + os.sep
        
        path_src = BaosAgent.path_src + str(freq) + '/'
        files = os.listdir(path_src)
        all_file_sto_id = []
        for file in files:
            if file.endswith('pkl'):
                all_file_sto_id.append(file[:6])

        NUM_PROCESS = 6
        size = math.ceil(len(all_file_sto_id) / NUM_PROCESS)

        sub_seqs = []
        for proc_idx in range(NUM_PROCESS):
            start_idx = size * proc_idx
            stop_idx = size * (proc_idx + 1)
            sub_seq = all_file_sto_id[start_idx:stop_idx]
            sub_seqs.append(sub_seq)

        with Pool(NUM_PROCESS) as pool:
            pool.map(partial(BaosAgent.complement_exist_data_proc, freq=freq), sub_seqs)

    @staticmethod
    def get_baostock_sto_id(sto_id):
        bs_sto_id = ''
        if sto_id.startswith('6'):
            bs_sto_id = 'sh.' + sto_id
        else:
            bs_sto_id = 'sz.' + sto_id
        return bs_sto_id  
    
    @staticmethod
    def get_freq_data_from_bs(sto_id, start_date, freq):
        bs.login()
        if sto_id.startswith('6'):
            bs_sto_id = 'sh.' + sto_id
        else:
            bs_sto_id = 'sz.' + sto_id
        
        if freq == 5:
            freq_str = str(freq)
        if freq == 15:
            freq_str = str(freq)
        if freq == 30:
            freq_str = str(freq)
        if freq == 60:
            freq_str = str(freq)
        if freq == 240:
            freq_str = 'd'
        if freq == 1200:
            freq_str = 'w'
        if freq == 4800:
            freq_str = 'm'
        
        if freq == 240:
            fields = "date,code,open,high,low,close,volume,turn,tradestatus"
        elif freq > 240:
            fields = "date,code,open,high,low,close,volume,turn"
        else:
            fields = "date,time,code,open,high,low,close,volume"
        
        end_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        # end_date = datetime.strftime(datetime.now()-timedelta(days=2), '%Y-%m-%d')
        
        rd = bs.query_history_k_data_plus(code=bs_sto_id,
                                          fields=fields,
                                          start_date=start_date,
                                          end_date=end_date,
                                          frequency=freq_str,
                                          adjustflag="2")
        df = rd.get_data()
        return df
    
    @staticmethod
    def persist_freq_data_proc(sub_sto_ids, start_date, freq):
        bs.login()
        
        fn_path = BaosAgent.path_src + str(freq) + os.sep
        daily_count = int(240/freq)
        min_size = 0
        if freq < 240:
            min_size = daily_count * 5 * 40

        # be sure there is enough data for compute monthly TA INDCATORS
        if freq == 240:
            min_size = 6 * 4 * 5
        if freq == 1200:
            min_size = 12 * 4
        if freq == 4800:
            min_size = 12
        
        for sto_id in tqdm(sub_sto_ids):
            fn = fn_path + sto_id + '.pkl'
            if os.path.exists(fn):
                ''' append data '''
                df = BaosAgent.read_freq_df(freq, sto_id)

                start_date = datetime.strftime(datetime.now() - timedelta(days = 7), '%Y-%m-%d')
                new_df = BaosAgent.get_freq_data_from_bs(sto_id, start_date, freq)
                if len(new_df) == 0:
                    print(sto_id, len(new_df))
                    continue
                if freq < 240:
                    new_df.time = new_df.time.str[:-5]
                    new_df.code = new_df.code.str[3:]
                    new_df[['open', 'high', 'low', 'close', 'volume']] =\
                        new_df[['open', 'high', 'low', 'close', 'volume']].astype(float)
                    new_df.open = np.round(new_df.open, 2)
                    new_df.high = np.round(new_df.high, 2)
                    new_df.low = np.round(new_df.low, 2)
                    new_df.close = np.round(new_df.close, 2)
                exist_times = df.time.values
                for idx in new_df.index:
                    new_data = new_df.iloc[idx]
                    if new_data.time not in exist_times:
                        df = df.append(new_data, ignore_index=True)
                df = df.reset_index(drop=True)
                df.to_pickle(fn, compression='xz')
            else:
                ''' create a new data file '''
                df = BaosAgent.get_freq_data_from_bs(sto_id, start_date, freq)
                if freq == 240:
                    try:
                        # df = df[df.tradestatus == '1']
                        # df = df.reset_index(drop=True)
                        df.loc[df.turn=='', 'turn'] = '0'
                        df = df.astype({'open':float, 'high':float, 'low':float, 'close':float, 'volume':float, 'turn':float, 'tradestatus':int})
                        # print(sto_id, len(df))
                    except Exception as e:
                        print(sto_id, e)
                        continue
                if len(df) >= min_size:
                    if freq < 240:
                        df.time = df.time.str[:-5]
                        df.code = df.code.str[3:]
                        df[['open', 'high', 'low', 'close', 'volume']] =\
                            df[['open', 'high', 'low', 'close', 'volume']].astype(float)
                        df.open = np.round(df.open, 2)
                        df.high = np.round(df.high, 2)
                        df.low = np.round(df.low, 2)
                        df.close = np.round(df.close, 2)
                    
                    df = df.reset_index(drop=True)
                    df.to_pickle(fn, compression='xz')
                else:
                    pass
                    # print('len(df): {} < {}'.format(len(df), min_size))
    
    def persist_freq_data(self, num_processes, start_date, freq):
        fn_path = BaosAgent.path_src + str(freq) + os.sep
        if not os.path.exists(fn_path):
            os.mkdir(fn_path)
        
        ###### FOR TEST
        # sid_list = random.sample(self.all_sids, 30)

        sid_list = self.all_sids
        size_req = math.ceil(len(sid_list) / num_processes)
        params = []
        for req_idx in range(num_processes):
            start_idx = req_idx * size_req
            stop_idx = (req_idx + 1) * size_req
            sub_sids = sid_list[start_idx: stop_idx]
            params.append(sub_sids)

        # Parallel Version
        with Pool(num_processes) as p:
            p.map(partial(BaosAgent.persist_freq_data_proc, start_date=start_date, freq=freq), params)

    @staticmethod
    def read_freq_df(freq, sto_id):
        fn = BaosAgent.path_src + str(freq) + os.sep + sto_id + '.pkl'
        df = pd.read_pickle(fn, compression='xz')
        return df

    @staticmethod
    def merge_df(org_df, freq, offset):
        remain = len(org_df) % offset
        if remain > 0:
            org_df = org_df[remain:]
            org_df = org_df.reset_index(drop=True)
        iis = pd.interval_range(start=0, end=len(org_df), freq=offset)
        dates = org_df.date.iloc[iis.right - 1].values
        if freq < 240:
            cols = ['date', 'time', 'code', 'open', 'high', 'low', 'close', 'volume']
            times = org_df.time.iloc[iis.right - 1].values
        if freq == 240:
            cols = ['date', 'code', 'open', 'high', 'low', 'close', 'volume', 'turn']
            turns = org_df.turn.rolling(window=offset).sum().iloc[range(offset - 1, len(org_df), offset)].values
        codes  = org_df.code.iloc[iis.right - 1].values
        opens  = org_df.open.iloc[iis.left].values
        closes = org_df.close.iloc[iis.right - 1].values
        highs  = org_df.high.rolling(window=offset).max().iloc[range(offset - 1, len(org_df), offset)].values
        lows   = org_df.low.rolling(window=offset).min().iloc[range(offset - 1, len(org_df), offset)].values
        vols   = org_df.volume.rolling(window=offset).sum().iloc[range(offset - 1, len(org_df), offset)].values

        datas = []
        for idx in range(len(dates)):
            if freq < 240:
                datas.append([dates[idx], times[idx], codes[idx], opens[idx], highs[idx], lows[idx], closes[idx], vols[idx]])
            if freq == 240:
                datas.append([dates[idx], codes[idx], opens[idx], highs[idx], lows[idx], closes[idx], vols[idx], turns[idx]])

        df_merged = pd.DataFrame(data=datas, columns=cols)
        return df_merged
    
    @staticmethod
    def get_current_endts():
        hms_list = [' 10:30:00', ' 11:30:00', ' 14:00:00', ' 15:00:00']
        today = datetime.strftime(datetime.now(), '%Y-%m-%d')
        yesterday = datetime.strftime(datetime.now() - timedelta(days = 1), '%Y-%m-%d')
        for idx in range(len(hms_list)):
            hms = hms_list[idx]
            hms_str = today + hms
            hms_time = datetime.strptime(hms_str, '%Y-%m-%d %H:%M:%S')
            if hms_time > datetime.now():
                if idx == 0:
                    return yesterday + hms_list[-1]
                else:
                    return today + hms_list[idx-1]
        return today + hms_list[-1]



class SinaDS:
    SIZE_PER_REQ = 800
    DF_COLUMNS   = ['st_id', 'st_name','tday_open_price','yday_close_price','curr_price','tday_max_price','tday_min_price','exc_shares','done_turnover','buy_1_shares','buy_1_price','buy_2_shares','buy_2_price','buy_3_shares','buy_3_price','buy_4_shares','buy_4_price','buy_5_shares','buy_5_price','sale_1_shares','sale_1_price','sale_2_shares','sale_2_price','sale_3_shares','sale_3_price','sale_4_shares','sale_4_price','sale_5_shares','sale_5_price','ts','change_percent']
    
    HTTP_URL_PRF = 'http://hq.sinajs.cn/list='
    HTTP_HEADERS = {'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                    }
    
    def __init__(self, sid_list):
        sina_sid_list = []
        for sid in sid_list:
            sina_sid = ''
            if sid.startswith('6'):
                sina_sid = 'sh' + sid
            else:
                sina_sid = 'sz' + sid
            sina_sid_list.append(sina_sid)
        self.st_ids = sina_sid_list
    
    def get_cur_all_df(self):
        st_slice_list = self.get_cur_all_slice_list()
        df = pd.DataFrame(data=st_slice_list, columns=SinaDS.DF_COLUMNS)
        
        return df

    def get_cur_all_slice_list(self):
        size_req      = math.ceil(len(self.st_ids) / SinaDS.SIZE_PER_REQ)
        st_slice_list = []
        for req_idx in range(size_req):
            start_idx = req_idx * SinaDS.SIZE_PER_REQ
            stop_idx  = (req_idx + 1) * SinaDS.SIZE_PER_REQ
            tmp_list = self._get_sub_cur_slice(self.st_ids[start_idx : stop_idx])
            st_slice_list.extend(tmp_list)
    
        return st_slice_list
    
    
    def get_cur_all_slice_dicts(self):
        st_slice_list = self.get_cur_all_slice_list()
        st_slice_dicts = []
        for st_slice in st_slice_list:
            st_slice_dict = dict(zip(SinaDS.DF_COLUMNS,st_slice))
            st_slice_dicts.append(st_slice_dict)
        
        return st_slice_dicts
    
    def get_cur_target_df(self, sid_list):
        
        df = None
        if len(sid_list) < SinaDS.SIZE_PER_REQ:
            target_list = self._get_sub_cur_slice(sid_list)
            df = pd.DataFrame(data=target_list, columns=SinaDS.DF_COLUMNS)
        else:
            size_req      = math.ceil(len(sid_list) / SinaDS.SIZE_PER_REQ)
            # print('requst size:{}'.format(size_req))
            st_slice_list = []
            for req_idx in range(size_req):
                ts1 = time.time()
                start_idx = req_idx * SinaDS.SIZE_PER_REQ
                stop_idx  = (req_idx + 1) * SinaDS.SIZE_PER_REQ
                tmp_list = self._get_sub_cur_slice(sid_list[start_idx : stop_idx])
                st_slice_list.extend(tmp_list)
                ts2 = time.time()
                print(req_idx, round(ts2 - ts1, 5))
            df = pd.DataFrame(data=st_slice_list, columns=SinaDS.DF_COLUMNS)
        return df
    
    def _get_sub_cur_slice(self, sub_sid_list):
        ''' WARNING: IT WILL SKIP DATA WITHOUT CURPRICE '''
        st_slice_list = []
        sids_str = ''
        for sid in sub_sid_list:
            sids_str += sid + ','
        sids_str = sids_str[:-1]
        url = SinaDS.HTTP_URL_PRF + sids_str
        # print(url)
        with requests.get(url, headers=SinaDS.HTTP_HEADERS, timeout=3) as response:
            resp_text = response.text
            # print(resp_text)
            rows_text = resp_text.split('\n')
#             rows_text.pop()
            # EXAMPLE DATA:
            #                          topen  yclose cp     
            # var hq_str_sz300429="XXX,32.880,32.810,34.450,34.990,32.650,34.440,34.450,10340128,354419713.770,4310,34.440,43900,34.430,84100,34.420,1200,34.410,2400,34.400,20433,34.450,5850,34.460,1900,34.470,1500,34.480,1400,34.500,2019-03-04,15:00:03,00";
            for row_text in rows_text:
                try:
                    resp_row_datas = row_text.split('=')
                    # print(resp_row_datas)
                    st_id = resp_row_datas[0][-8:]
                    row_data = resp_row_datas[1][1:-5].split(',')
                    # print(row_data)
                    del(row_data[6:8])
                    st_name          = row_data[0]          # st_name         
                    tday_open_price  = float(row_data[1])   # tday_open_price 
                    yday_close_price = float(row_data[2])   # yday_close_price
                    curr_price       = float(row_data[3])   # curr_price      
                    if curr_price == 0:
                        continue
                    tday_max_price   = float(row_data[4])   # tday_max_price  
                    tday_min_price   = float(row_data[5])   # tday_min_price  
                    exc_shares       = float(row_data[6])   # exc_shares      
                    done_turnover    = float(row_data[7])   # done_turnover   
                    buy_1_shares     = int(row_data[8])     # buy_1_shares    
                    buy_1_price      = float(row_data[9])   # buy_1_price     
                    buy_2_shares     = int(row_data[10])    # buy_2_shares    
                    buy_2_price      = float(row_data[11])  # buy_2_price     
                    buy_3_shares     = int(row_data[12])    # buy_3_shares    
                    buy_3_price      = float(row_data[13])  # buy_3_price     
                    buy_4_shares     = int(row_data[14])    # buy_4_shares    
                    buy_4_price      = float(row_data[15])  # buy_4_price     
                    buy_5_shares     = int(row_data[16])    # buy_5_shares    
                    buy_5_price      = float(row_data[17])  # buy_5_price     
                    sale_1_shares    = int(row_data[18])    # sale_1_shares   
                    sale_1_price     = float(row_data[19])  # sale_1_price    
                    sale_2_shares    = int(row_data[20])    # sale_2_shares   
                    sale_2_price     = float(row_data[21])  # sale_2_price    
                    sale_3_shares    = int(row_data[22])    # sale_3_shares   
                    sale_3_price     = float(row_data[23])  # sale_3_price    
                    sale_4_shares    = int(row_data[24])    # sale_4_shares   
                    sale_4_price     = float(row_data[25])  # sale_4_price    
                    sale_5_shares    = int(row_data[26])    # sale_5_shares   
                    sale_5_price     = float(row_data[27])  # sale_5_price  
                    timestamp        = row_data[28] + ' ' + row_data[29] # date, time
                    ts               = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    change_percent   = (curr_price - yday_close_price) * 100 /yday_close_price
                    # print([st_id,st_name,tday_open_price,yday_close_price,curr_price,tday_max_price,tday_min_price,exc_shares,done_turnover,buy_1_shares,buy_1_price,buy_2_shares,buy_2_price,buy_3_shares,buy_3_price,buy_4_shares,buy_4_price,buy_5_shares,buy_5_price,sale_1_shares,sale_1_price,sale_2_shares,sale_2_price,sale_3_shares,sale_3_price,sale_4_shares,sale_4_price,sale_5_shares,sale_5_price,ts,change_percent])
                    st_slice_list.append([st_id,st_name,tday_open_price,yday_close_price,curr_price,tday_max_price,tday_min_price,exc_shares,done_turnover,buy_1_shares,buy_1_price,buy_2_shares,buy_2_price,buy_3_shares,buy_3_price,buy_4_shares,buy_4_price,buy_5_shares,buy_5_price,sale_1_shares,sale_1_price,sale_2_shares,sale_2_price,sale_3_shares,sale_3_price,sale_4_shares,sale_4_price,sale_5_shares,sale_5_price,ts,change_percent])
                except Exception as e:
                    pass
        return st_slice_list
    
    def get_today_info(self, sid):
        sina_sid = sid
        if sina_sid.startswith('6'):
            sina_sid = 'sh' + sina_sid
        else:
            sina_sid = 'sz' + sina_sid

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        response = requests.get('http://hq.sinajs.cn/list='+sina_sid, headers=headers)
        raw_today_info = response.text.split('=')[1]
        raw_today_info = raw_today_info.split(',')
        # top, ycp, cp, maxp, minp, ts
        return float(raw_today_info[1]), float(raw_today_info[2]), float(raw_today_info[3]), float(raw_today_info[4]), float(raw_today_info[5]), raw_today_info[-2]

class JQDataUtil:

    @staticmethod
    def get_jq_stoid(sto_id):
        if sto_id.startswith('6'):
            jq_sto_id = sto_id + '.XSHG'
        else:
            jq_sto_id = sto_id + '.XSHE'
        return jq_sto_id
    
    @staticmethod
    def get_end_ts(delta):
        hms_list = []
        if delta == 30:
            hms_list = [' 10:00:00', ' 10:30:00', ' 11:00:00', ' 11:30:00', ' 13:30:00', ' 14:00:00', ' 14:30:00', ' 15:00:00']
        if delta == 15:
            hms_list = [' 09:45:00', ' 10:00:00', ' 10:15:00', ' 10:30:00', ' 10:45:00', ' 11:00:00', ' 11:15:00', ' 11:30:00',\
                        ' 13:15:00', ' 13:30:00', ' 13:45:00', ' 14:00:00', ' 14:15:00', ' 14:30:00', ' 14:45:00', ' 15:00:00']
        if delta == 5:
            hms_list = [' 09:35:00', ' 09:40:00', ' 09:45:00', ' 09:50:00', ' 09:55:00', ' 10:00:00', ' 10:05:00', ' 10:10:00',\
                        ' 10:15:00', ' 10:20:00', ' 10:25:00', ' 10:30:00', ' 10:35:00', ' 10:40:00', ' 10:45:00', ' 10:50:00',\
                        ' 10:55:00', ' 11:00:00', ' 11:05:00', ' 11:10:00', ' 11:15:00', ' 11:20:00', ' 11:25:00', ' 11:30:00',\
                        ' 13:05:00', ' 13:10:00', ' 13:15:00', ' 13:20:00', ' 13:25:00', ' 13:30:00', ' 13:35:00', ' 13:40:00',\
                        ' 13:45:00', ' 13:50:00', ' 13:55:00', ' 14:00:00', ' 14:05:00', ' 14:10:00', ' 14:15:00', ' 14:20:00',\
                        ' 14:25:00', ' 14:30:00', ' 14:35:00', ' 14:40:00', ' 14:45:00', ' 14:50:00', ' 14:55:00', ' 15:00:00']

        today = datetime.strftime(datetime.now(), '%Y-%m-%d')
        yesterday = datetime.strftime(datetime.now() - timedelta(days = 1), '%Y-%m-%d')
        for idx in range(len(hms_list)):
            hms = hms_list[idx]
            hms_str = today + hms
            hms_time = datetime.strptime(hms_str, '%Y-%m-%d %H:%M:%S')
            if hms_time > datetime.now():
                if idx == 0:
                    return yesterday + hms_list[-1]
                else:
                    return today + hms_list[idx-1]
        end_ts =  today + hms_list[-1]
        return(end_ts)

class DataUtil:
    
    @staticmethod
    def get_freq_file_sto_ids(freq):
        file_sto_ids = []
        path_src = './data/' + str(freq) + '/'
        files = os.listdir(path_src)
        all_file_sto_id = []
        for file in files:
            if file.endswith('pkl'):
                file_sto_ids.append(file[:6])
        return file_sto_ids
    
    @staticmethod
    def add_rt_data(sto_id, org_df, delta, ts_jq):
        daily_count = int(240/delta)
        jq_sto_id = JQDataUtil.get_jq_stoid(sto_id)
        df_rt = jq.get_price(jq_sto_id, count = daily_count * 3, end_date=ts_jq, frequency=str(delta) + 'm', fields=['open','high','low','close','volume'])
        df_rt.insert(0, 'code', sto_id)
        df_rt.insert(0, 'time', pd.Series(df_rt.index).dt.strftime('%Y%m%d%H%M').values)
        df_rt.insert(0, 'date', pd.Series(df_rt.index).dt.strftime('%Y-%m-%d').values)
        df_rt = df_rt.reset_index(drop=True)
        exist_times = org_df.time.values
        for idx in df_rt.index:
            new_data = df_rt.iloc[idx]
            if new_data.time not in exist_times:
                org_df = org_df.append(new_data, ignore_index=True)
        return org_df

if __name__ == "__main__":
    jq.auth('15808061188', 'allan2jq')
    all_securities = jq.get_all_securities(date=datetime.now())
    all_securities = all_securities[all_securities.display_name.str.find('ST') == -1]
    all_securities = all_securities[all_securities.display_name.str.find('退') == -1]
    all_securities = all_securities[all_securities.index.str.startswith('688') == False]
    all_sto_id = all_securities.index.str[:6].to_list()

    bs_agent = BaosAgent(all_sto_id)
    freq = 15
    start_date = '2020-03-01'
    num_processes = 6
    
    data_path = bs_agent.path_src+str(freq) + os.path.sep
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    bs_agent.persist_freq_data(num_processes, start_date, freq)
