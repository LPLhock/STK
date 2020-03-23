#coding=utf-8

import os
import math
import talib
import pandas as pd
import jqdatasdk as jq
import matplotlib.pyplot as plt

from multiprocessing import Pool
from functools import partial
from tqdm import tqdm
from datetime import datetime
from datagent import BaosAgent
from datagent import DataUtil
from datagent import JQDataUtil
from featureutils import FeatureTool
from plotutils import PlotTool


class SFStrategy:

    def __init__(self, delta):
        self.delta = delta
        self.daily_count = int(240 / self.delta)
        self.sto_ids = DataUtil.get_freq_file_sto_ids(self.delta)

    def add_macd_indicators(self, df):
        ''' minimum data size: 11198 '''
        # factor_9t = self.daily_count * 25
        factor_8t = self.daily_count * 20
        factor_7t = self.daily_count * 15
        factor_6t = self.daily_count * 10
        factor_5t = self.daily_count * 5
        factor_4t = self.daily_count * 4
        factor_3t = self.daily_count * 3
        factor_2t = self.daily_count * 2
        factor_1t = self.daily_count * 1
        factor_1h = 4
        
        # df['macd_9t'], df['macdsignal_9t'], df['machhist_9t'] = talib.MACD(df.close, fastperiod=12*factor_9t, slowperiod=26*factor_9t, signalperiod=9*factor_9t)
        df['macd_8t'], df['macdsignal_8t'], df['machhist_8t'] = talib.MACD(df.close, fastperiod=12*factor_8t, slowperiod=26*factor_8t, signalperiod=9*factor_8t)
        df['macd_7t'], df['macdsignal_7t'], df['machhist_7t'] = talib.MACD(df.close, fastperiod=12*factor_7t, slowperiod=26*factor_7t, signalperiod=9*factor_7t)
        df['macd_6t'], df['macdsignal_6t'], df['machhist_6t'] = talib.MACD(df.close, fastperiod=12*factor_6t, slowperiod=26*factor_6t, signalperiod=9*factor_6t)
        df['macd_5t'], df['macdsignal_5t'], df['machhist_5t'] = talib.MACD(df.close, fastperiod=12*factor_5t, slowperiod=26*factor_5t, signalperiod=9*factor_5t)
        df['macd_4t'], df['macdsignal_4t'], df['machhist_4t'] = talib.MACD(df.close, fastperiod=12*factor_4t, slowperiod=26*factor_4t, signalperiod=9*factor_4t)
        df['macd_3t'], df['macdsignal_3t'], df['machhist_3t'] = talib.MACD(df.close, fastperiod=12*factor_3t, slowperiod=26*factor_3t, signalperiod=9*factor_3t)
        df['macd_2t'], df['macdsignal_2t'], df['machhist_2t'] = talib.MACD(df.close, fastperiod=12*factor_2t, slowperiod=26*factor_2t, signalperiod=9*factor_2t)
        df['macd_1t'], df['macdsignal_1t'], df['machhist_1t'] = talib.MACD(df.close, fastperiod=12*factor_1t, slowperiod=26*factor_1t, signalperiod=9*factor_1t)
        df['macd_1h'], df['macdsignal_1h'], df['machhist_1h'] = talib.MACD(df.close, fastperiod=12*factor_1h, slowperiod=26*factor_1h, signalperiod=9*factor_1h)
        
        return df

    def add_strategy_features(self, df):
        ### reduce compute data size ###
        df = df.iloc[-self.daily_count * 125:].copy()
        ################################

        factor_9t = 6 * 9
        factor_8t = 6 * 8
        factor_7t = 6 * 7
        factor_6t = 6 * 6
        factor_5t = 6 * 5
        factor_4t = 6 * 4
        factor_3t = 6 * 3
        factor_2t = 6 * 2
        factor_1t = 6 * 1

        df['k_9t'], df['d_9t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_9t, slowk_period=3*factor_9t, slowd_period=3*factor_9t)
        df['k_8t'], df['d_8t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_8t, slowk_period=3*factor_8t, slowd_period=3*factor_8t)
        df['k_7t'], df['d_7t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_7t, slowk_period=3*factor_7t, slowd_period=3*factor_7t)
        df['k_6t'], df['d_6t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_6t, slowk_period=3*factor_6t, slowd_period=3*factor_6t)
        df['k_5t'], df['d_5t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_5t, slowk_period=3*factor_5t, slowd_period=3*factor_5t)
        df['k_4t'], df['d_4t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_4t, slowk_period=3*factor_4t, slowd_period=3*factor_4t)
        df['k_3t'], df['d_3t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_3t, slowk_period=3*factor_3t, slowd_period=3*factor_3t)
        df['k_2t'], df['d_2t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_2t, slowk_period=3*factor_2t, slowd_period=3*factor_2t)
        df['k_1t'], df['d_1t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_1t, slowk_period=3*factor_1t, slowd_period=3*factor_1t)
        return df
    
    @staticmethod
    def get_cond_k12345above80_last40(df, daily_count):
        cond = ((df.K_1 > 80) | (df.K_2 > 80) | (df.K_3 > 80) | (df.K_4 > 80) | (df.K_5 > 80) | (df.K_6 > 80) | (df.K_7 > 80) | (df.K_8 > 80)).rolling(daily_count * 2).apply(lambda x: x.all(), raw=True) == 1
        cond = (df.K_1.diff(1) < 0) & (df.K_1.diff(-1) < 0) & cond
        
        return cond

    @staticmethod
    def get_cond_ksumavg_cross60(df):
        cond = (df.KSUM_AVG > 60) & (df.KSUM_AVG.shift(1) < 60)
        return cond

    @staticmethod
    def compute_cond_long(k, d):
        cond_long  = (k > d) & (k > 20) | (k > 80)
        return cond_long

    def compute_longshort_index(self, record):
        long = 0
        if record.k_qut > record.d_qut and record.k_qut > 20 or record.k_qut > 80:
            long += 4
        if record.k_mon > record.d_mon and record.d_mon > 20 or record.d_mon > 80:
            long += 3
        if record.k_wek > record.d_wek and record.d_wek > 20 or record.d_wek > 80:
            long += 2
        if record.k_day > record.d_day and record.d_day > 20 or record.d_day > 80:
            long += 1
        
        short = 0
        if record.k_qut < record.d_qut and record.k_qut < 80 or record.k_qut < 20:
            short += 4
        if record.k_mon < record.d_mon and record.d_mon < 80 or record.d_mon < 20:
            short += 3
        if record.k_wek < record.d_wek and record.d_wek < 80 or record.d_wek < 20:
            short += 2
        if record.k_day < record.d_day and record.d_day < 80 or record.d_day < 20:
            short += 1

        return long, short

    def save_match_pics(self, sto_id, pic_path, ts_jq):
        df = BaosAgent.read_freq_df(self.delta, sto_id)
        df = DataUtil.add_rt_data(sto_id, df, self.delta, ts_jq)
        df = FeatureTool.add_ta_features(df, self.daily_count)
        df = FeatureTool.add_close_features(df, self.daily_count)
        df = df.dropna()
        df = df.reset_index(drop=True)
        minimum = self.daily_count*5*24
        if len(df) >= minimum:
            df = df.iloc[-minimum:]
            df = df.reset_index(drop=True)
            cond = SFStrategy.get_cond_k12345above80_last40(df, self.daily_count)
            tgt_idxes = df[cond].index
            print('df size:' + str(len(df)))
            PlotTool.display_obs(df, self.daily_count, tgt_idxes, True, pic_path)
    
    def find_matches(self, num_processes, enable_realtime, ts_fn, ts_jq):
        # self.sto_ids = ['002050']

        size = math.ceil(len(self.sto_ids) / num_processes)
        sub_sto_ids_list = []
        for proc_idx in range(num_processes):
            start_idx = size * proc_idx
            stop_idx = size * (proc_idx + 1)
            sub_sto_ids = self.sto_ids[start_idx:stop_idx]
            sub_sto_ids_list.append(sub_sto_ids)
        # print(sub_sto_ids_list)
        with Pool(num_processes) as pool:
            rlts = pool.map(partial(self.find_matches_subprocess, enable_realtime=enable_realtime, ts_fn=ts_fn, ts_jq=ts_jq), sub_sto_ids_list)
            pool.close()
            pool.join()
            
            match_infos = []
            for rlt in rlts:
                for target in rlt:
                    match_infos.append(target)
            print('match size: ' + str(len(match_infos)))
            matches_df = pd.DataFrame(columns=['sto_id', 'lastest_match_ts', 'lastest_close', 'last_hyear_cr', 'last_quart_cr', 'last_month_cr', 'last_week_cr', 'close'], data=match_infos)
            matches_df = matches_df.sort_values(by=['sto_id'])
            matches_path = './target/'
            if not os.path.exists(matches_path):
                os.mkdir(matches_path)
            matches_df.to_csv(matches_path+'matches_'+ts_fn+'.csv', index=False)

    def find_matches_subprocess(self, sub_sto_ids, enable_realtime, ts_fn, ts_jq):
        if enable_realtime:
            login = jq.auth('15808061188', 'allan2jq')
        
        match_infos = []
        minimum_df_size = self.daily_count * 5 * 20
        for sto_id in sub_sto_ids:
            try:
                df = BaosAgent.read_freq_df(self.delta, sto_id)
                ### add_macd_indicators minimum data size: 11198
                if len(df) < 11198:
                    continue
                
                curp = df.iloc[-1].close
                if curp > 50:
                    continue

                if enable_realtime:
                    df = DataUtil.add_rt_data(sto_id, df, self.delta, ts_jq)
                # df = df.iloc[-self.daily_count * 5 * 30:]
                # df = df.reset_index(drop=True)
                # df = self.add_strategy_features(df)
                df = self.add_macd_indicators(df)
                df = df.dropna()
                df = df.reset_index(drop=True)

                last_week_minp = min(df.close.iloc[-self.daily_count * 5:])
                last_week_cr = (curp - last_week_minp) / last_week_minp
                last_month_minp = min(df.close.iloc[-self.daily_count * 20:])
                last_month_cr = (curp - last_month_minp) / last_month_minp
                last_quart_minp = min(df.close.iloc[-self.daily_count * 60:])
                last_quart_cr = (curp - last_quart_minp) / last_quart_minp
                last_hyear_minp = min(df.close.iloc[-self.daily_count * 120:])
                last_hyear_cr = (curp - last_hyear_minp) / last_hyear_minp
                # if last_hyear_cr > .5: # and last_quart_cr < .5 and last_month_cr < .3 and last_week_cr < .2# and last_quart_cr < .5 and last_month_cr < .3 and last_week_cr < .2 :
                #     continue
                
                # cond_long_9t = SFStrategy.compute_cond_long(df.k_9t, df.d_9t)
                # cond_long_8t = SFStrategy.compute_cond_long(df.k_8t, df.d_8t)
                # cond_long_7t = SFStrategy.compute_cond_long(df.k_7t, df.d_7t)
                # cond_long_6t = SFStrategy.compute_cond_long(df.k_6t, df.d_6t)
                # cond_long_5t = SFStrategy.compute_cond_long(df.k_5t, df.d_5t)
                # cond_long_4t = SFStrategy.compute_cond_long(df.k_4t, df.d_4t)
                # cond_long_3t = SFStrategy.compute_cond_long(df.k_3t, df.d_3t)
                # cond_long_2t = SFStrategy.compute_cond_long(df.k_2t, df.d_2t)
                # cond_long_1t = SFStrategy.compute_cond_long(df.k_1t, df.d_1t)
                # cond_all_long = cond_long_1t & cond_long_2t & cond_long_3t & cond_long_4t & cond_long_5t & cond_long_6t & cond_long_7t & cond_long_8t & cond_long_9t

                # if not (cond_all_long.iloc[-2]) and cond_all_long.iloc[-1]:
                cond_macd_allabove0 = (df.macd_1h > 0) & (df.macd_1t > 0) & (df.macd_2t > 0) & (df.macd_3t > 0) & (df.macd_4t > 0) & (df.macd_5t > 0)
                if len(cond_macd_allabove0) > 0 and not cond_macd_allabove0.iloc[-2] and cond_macd_allabove0.iloc[-1]:
                    target_t = df.time.iloc[-1]
                    print('{} {} {:>5.2f} {:>7.2%} {:>7.2%} {:>7.2%} {:>7.2%}'.format(sto_id, target_t, curp, last_hyear_cr, last_quart_cr, last_month_cr, last_week_cr))
                    match_infos.append([sto_id, target_t, curp, last_hyear_cr, last_quart_cr, last_month_cr, last_week_cr, curp])
            except Exception as e:
                # print(sto_id, e)
                pass
        
        # if enable_realtime:
        #     jq.logout()
        return match_infos


if __name__ == "__main__":
    b_time = datetime.now()

    delta = 15
    sfs = SFStrategy(delta)
    num_processes = 5
    enable_realtime = True
    ts_fn = ''
    ts_jq = JQDataUtil.get_end_ts(delta)
    if enable_realtime:
        ts = datetime.strptime(ts_jq, '%Y-%m-%d %H:%M:%S')
    else:
        ts = datetime.now()
    ts_fn = datetime.strftime(ts, '%Y-%m-%d-%H%M')
    print('Find out:' + ts_fn)
    sfs.find_matches(num_processes, enable_realtime, ts_fn, ts_jq)
    # sfs.save_match_pics()
    e_time = datetime.now()
    print('Last time: ' + str(e_time - b_time))
