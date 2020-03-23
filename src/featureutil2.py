#coding=utf-8

import numpy as np
import pandas as pd
import talib

class FeatureTool:

    @staticmethod
    def add_kds_indicators(df, daily_count):
        factor_01d = daily_count * 1
        factor_02d = daily_count * 2
        factor_03d = daily_count * 3
        factor_04d = daily_count * 4
        factor_05d = daily_count * 5
        factor_06d = daily_count * 6
        factor_07d = daily_count * 7
        factor_08d = daily_count * 8
        factor_09d = daily_count * 9
        factor_10d = daily_count * 10
        factor_11d = daily_count * 11
        factor_12d = daily_count * 12
        factor_13d = daily_count * 13
        factor_14d = daily_count * 14
        factor_15d = daily_count * 15
        factor_16d = daily_count * 16
        factor_17d = daily_count * 17
        factor_18d = daily_count * 18
        factor_19d = daily_count * 19
        factor_20d = daily_count * 20
        factor_21d = daily_count * 21
        factor_22d = daily_count * 22
        factor_23d = daily_count * 23
        factor_24d = daily_count * 24
        factor_25d = daily_count * 25
        factor_26d = daily_count * 26
        factor_27d = daily_count * 27
        factor_28d = daily_count * 28
        factor_29d = daily_count * 29
        factor_30d = daily_count * 30


        factor_3h = int(3 * daily_count / 4)
        factor_2h = int(daily_count/2)
        factor_1h = int(daily_count/4)
        factor_hh = int(daily_count/8)
        factor_1t = 1

        df['k_1t'], df['d_1t'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_1t, slowk_period=3*factor_1t, slowd_period=3*factor_1t)
        df['k_1h'], df['d_1h'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_1h, slowk_period=3*factor_1h, slowd_period=3*factor_1h)

        df['k_01d'], df['d_01d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_01d, slowk_period=3*factor_01d, slowd_period=3*factor_01d)
        df['k_02d'], df['d_02d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_02d, slowk_period=3*factor_02d, slowd_period=3*factor_02d)
        df['k_03d'], df['d_03d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_03d, slowk_period=3*factor_03d, slowd_period=3*factor_03d)
        df['k_04d'], df['d_04d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_04d, slowk_period=3*factor_04d, slowd_period=3*factor_04d)
        df['k_05d'], df['d_05d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_05d, slowk_period=3*factor_05d, slowd_period=3*factor_05d)
        df['k_06d'], df['d_06d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_06d, slowk_period=3*factor_06d, slowd_period=3*factor_06d)
        df['k_07d'], df['d_07d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_07d, slowk_period=3*factor_07d, slowd_period=3*factor_07d)
        df['k_08d'], df['d_08d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_08d, slowk_period=3*factor_08d, slowd_period=3*factor_08d)
        df['k_09d'], df['d_09d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_09d, slowk_period=3*factor_09d, slowd_period=3*factor_09d)
        df['k_10d'], df['d_10d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_10d, slowk_period=3*factor_10d, slowd_period=3*factor_10d)
        df['k_11d'], df['d_11d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_11d, slowk_period=3*factor_11d, slowd_period=3*factor_11d)
        df['k_12d'], df['d_12d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_12d, slowk_period=3*factor_12d, slowd_period=3*factor_12d)
        df['k_13d'], df['d_13d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_13d, slowk_period=3*factor_13d, slowd_period=3*factor_13d)
        df['k_14d'], df['d_14d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_14d, slowk_period=3*factor_14d, slowd_period=3*factor_14d)
        df['k_15d'], df['d_15d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_15d, slowk_period=3*factor_15d, slowd_period=3*factor_15d)
        df['k_16d'], df['d_16d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_16d, slowk_period=3*factor_16d, slowd_period=3*factor_16d)
        df['k_17d'], df['d_17d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_17d, slowk_period=3*factor_17d, slowd_period=3*factor_17d)
        df['k_18d'], df['d_18d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_18d, slowk_period=3*factor_18d, slowd_period=3*factor_18d)
        df['k_19d'], df['d_19d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_19d, slowk_period=3*factor_19d, slowd_period=3*factor_19d)
        df['k_20d'], df['d_20d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_20d, slowk_period=3*factor_20d, slowd_period=3*factor_20d)
        df['k_21d'], df['d_21d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_21d, slowk_period=3*factor_21d, slowd_period=3*factor_21d)
        df['k_22d'], df['d_22d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_22d, slowk_period=3*factor_22d, slowd_period=3*factor_22d)
        df['k_23d'], df['d_23d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_23d, slowk_period=3*factor_23d, slowd_period=3*factor_23d)
        df['k_24d'], df['d_24d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_24d, slowk_period=3*factor_24d, slowd_period=3*factor_24d)
        df['k_25d'], df['d_25d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_25d, slowk_period=3*factor_25d, slowd_period=3*factor_25d)
        df['k_26d'], df['d_26d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_26d, slowk_period=3*factor_26d, slowd_period=3*factor_26d)
        df['k_27d'], df['d_27d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_27d, slowk_period=3*factor_27d, slowd_period=3*factor_27d)
        df['k_28d'], df['d_28d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_28d, slowk_period=3*factor_28d, slowd_period=3*factor_28d)
        df['k_29d'], df['d_29d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_29d, slowk_period=3*factor_29d, slowd_period=3*factor_29d)
        df['k_30d'], df['d_30d'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9*factor_30d, slowk_period=3*factor_30d, slowd_period=3*factor_30d)
        
        df['k_sum'] = 0
        for col in df.columns:
            if col.startswith('k_') and col.endswith('d'):
                df['k_sum'] += df[col]
        df['k_sum'] /= 30
        
        df['ksum_last_0hh'] = (df.k_1t - 50).rolling(factor_hh).sum()
        df['ksum_last_01h'] = (df.k_1t - 50).rolling(factor_1h).sum()
        df['ksum_last_02h'] = (df.k_1t - 50).rolling(factor_2h).sum()
        df['ksum_last_03h'] = (df.k_1t - 50).rolling(factor_3h).sum()
        df['ksum_last_01d'] = (df.k_1t - 50).rolling(daily_count * 1).sum()
        df['ksum_last_02d'] = (df.k_1t - 50).rolling(daily_count * 2).sum()
        df['ksum_last_03d'] = (df.k_1t - 50).rolling(daily_count * 3).sum()
        df['ksum_last_04d'] = (df.k_1t - 50).rolling(daily_count * 4).sum()
        df['ksum_last_01w'] = (df.k_1t - 50).rolling(daily_count * 5 *  1).sum()
        df['ksum_last_02w'] = (df.k_1t - 50).rolling(daily_count * 5 *  2).sum()
        df['ksum_last_03w'] = (df.k_1t - 50).rolling(daily_count * 5 *  3).sum()
        df['ksum_last_04w'] = (df.k_1t - 50).rolling(daily_count * 5 *  4).sum()
        df['ksum_last_08w'] = (df.k_1t - 50).rolling(daily_count * 5 *  8).sum()
        df['ksum_last_12w'] = (df.k_1t - 50).rolling(daily_count * 5 * 12).sum()
        df['ksum_last_16w'] = (df.k_1t - 50).rolling(daily_count * 5 * 16).sum()
        df['ksum_last_20w'] = (df.k_1t - 50).rolling(daily_count * 5 * 20).sum()
        df['ksum_last_24w'] = (df.k_1t - 50).rolling(daily_count * 5 * 24).sum()
        return df

    @staticmethod
    def add_mfi_indicators(df, daily_count):
        # factor_1h = int(daily_count/4)
        factor_01d = daily_count * 1
        factor_02d = daily_count * 2
        factor_03d = daily_count * 3
        factor_04d = daily_count * 4
        factor_05d = daily_count * 5
        factor_06d = daily_count * 6
        factor_07d = daily_count * 7
        factor_08d = daily_count * 8
        factor_09d = daily_count * 9
        factor_10d = daily_count * 10
        factor_11d = daily_count * 11
        factor_12d = daily_count * 12
        factor_13d = daily_count * 13
        factor_14d = daily_count * 14
        factor_15d = daily_count * 15
        factor_16d = daily_count * 16
        factor_17d = daily_count * 17
        factor_18d = daily_count * 18
        factor_19d = daily_count * 19
        factor_20d = daily_count * 20
        factor_21d = daily_count * 21
        factor_22d = daily_count * 22
        factor_23d = daily_count * 23
        factor_24d = daily_count * 24
        factor_25d = daily_count * 25
        factor_26d = daily_count * 26
        factor_27d = daily_count * 27
        factor_28d = daily_count * 28
        factor_29d = daily_count * 29
        factor_30d = daily_count * 30

        df['mfi_01d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_01d)
        df['mfi_02d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_02d)
        df['mfi_03d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_03d)
        df['mfi_04d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_04d)
        df['mfi_05d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_05d)
        df['mfi_06d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_06d)
        df['mfi_07d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_07d)
        df['mfi_08d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_08d)
        df['mfi_09d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_09d)
        df['mfi_10d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_10d)
        df['mfi_11d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_11d)
        df['mfi_12d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_12d)
        df['mfi_13d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_13d)
        df['mfi_14d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_14d)
        df['mfi_15d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_15d)
        df['mfi_16d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_16d)
        df['mfi_17d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_17d)
        df['mfi_18d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_18d)
        df['mfi_19d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_19d)
        df['mfi_20d'] = talib.MFI(df.high, df.low, df.close, np.log(df.volume + 1000), timeperiod=factor_20d)
        
        return df

    @staticmethod
    def add_volma_indicators(df, daily_count):
        factor_4w = daily_count * 20
        factor_3w = daily_count * 15
        factor_2w = daily_count * 10
        factor_5d = daily_count * 5
        factor_4d = daily_count * 4
        factor_3d = daily_count * 3
        factor_2d = daily_count * 2
        factor_1d = daily_count * 1
        factor_1h = int(daily_count/4)
        
        df.loc[df.volume==0, 'volume'] = 5000
        df.volume = df.volume/10000

        df['vol_log_ma_4w'] = talib.MA(np.log(df.volume), timeperiod=factor_4w)
        df['vol_log_ma_3w'] = talib.MA(np.log(df.volume), timeperiod=factor_3w)
        df['vol_log_ma_2w'] = talib.MA(np.log(df.volume), timeperiod=factor_2w)
        df['vol_log_ma_5d'] = talib.MA(np.log(df.volume), timeperiod=factor_5d)
        df['vol_log_ma_4d'] = talib.MA(np.log(df.volume), timeperiod=factor_4d)
        df['vol_log_ma_3d'] = talib.MA(np.log(df.volume), timeperiod=factor_3d)
        df['vol_log_ma_2d'] = talib.MA(np.log(df.volume), timeperiod=factor_2d)
        df['vol_log_ma_1d'] = talib.MA(np.log(df.volume), timeperiod=factor_1d)
        df['vol_log_ma_1h'] = talib.MA(np.log(df.volume), timeperiod=factor_1h)
        df['vol_log_ma_avg'] = (df.vol_log_ma_1h + df.vol_log_ma_1d*4 + df.vol_log_ma_2d*8 + df.vol_log_ma_3d*12 + df.vol_log_ma_4d*16 + df.vol_log_ma_5d*20 + df.vol_log_ma_2w*40 + df.vol_log_ma_3w*60 + df.vol_log_ma_4w*80) / (1+4+8+12+16+20+40+60+80)
        
        df['vol_ma_4w'] = talib.MA(df.volume, timeperiod=factor_4w)
        df['vol_ma_3w'] = talib.MA(df.volume, timeperiod=factor_3w)
        df['vol_ma_2w'] = talib.MA(df.volume, timeperiod=factor_2w)
        df['vol_ma_5d'] = talib.MA(df.volume, timeperiod=factor_5d)
        df['vol_ma_4d'] = talib.MA(df.volume, timeperiod=factor_4d)
        df['vol_ma_3d'] = talib.MA(df.volume, timeperiod=factor_3d)
        df['vol_ma_2d'] = talib.MA(df.volume, timeperiod=factor_2d)
        df['vol_ma_1d'] = talib.MA(df.volume, timeperiod=factor_1d)
        df['vol_ma_1h'] = talib.MA(df.volume, timeperiod=factor_1h)
        df['vol_ma_avg'] = (df.vol_ma_1h + df.vol_ma_1d*4 + df.vol_ma_2d*8 + df.vol_ma_3d*12 + df.vol_ma_4d*16 + df.vol_ma_5d*20 + df.vol_ma_2w*40 + df.vol_ma_3w*60 + df.vol_ma_4w*80) / (1+4+8+12+16+20+40+60+80)
        return df

    @staticmethod
    def add_vol_sum(df, daily_count):
        df['vol_1t_sum_last_01d'] = df.volume.rolling(daily_count * 1).sum()
        df['vol_1t_sum_last_02d'] = df.volume.rolling(daily_count * 2).sum()
        df['vol_1t_sum_last_03d'] = df.volume.rolling(daily_count * 3).sum()
        df['vol_1t_sum_last_04d'] = df.volume.rolling(daily_count * 4).sum()
        df['vol_1t_sum_last_01w'] = df.volume.rolling(daily_count * 5 *  1).sum()
        df['vol_1t_sum_last_02w'] = df.volume.rolling(daily_count * 5 *  2).sum()
        df['vol_1t_sum_last_03w'] = df.volume.rolling(daily_count * 5 *  3).sum()
        df['vol_1t_sum_last_04w'] = df.volume.rolling(daily_count * 5 *  4).sum()
        df['vol_1t_sum_last_05w'] = df.volume.rolling(daily_count * 5 *  5).sum()
        df['vol_1t_sum_last_06w'] = df.volume.rolling(daily_count * 5 *  6).sum()
        df['vol_1t_sum_last_07w'] = df.volume.rolling(daily_count * 5 *  7).sum()
        df['vol_1t_sum_last_08w'] = df.volume.rolling(daily_count * 5 *  8).sum()
        df['vol_1t_sum_last_09w'] = df.volume.rolling(daily_count * 5 *  9).sum()
        df['vol_1t_sum_last_10w'] = df.volume.rolling(daily_count * 5 * 10).sum()
        df['vol_1t_sum_last_11w'] = df.volume.rolling(daily_count * 5 * 11).sum()
        df['vol_1t_sum_last_12w'] = df.volume.rolling(daily_count * 5 * 12).sum()
        df['vol_1t_sum_last_13w'] = df.volume.rolling(daily_count * 5 * 13).sum()
        df['vol_1t_sum_last_14w'] = df.volume.rolling(daily_count * 5 * 14).sum()
        df['vol_1t_sum_last_15w'] = df.volume.rolling(daily_count * 5 * 15).sum()
        df['vol_1t_sum_last_16w'] = df.volume.rolling(daily_count * 5 * 16).sum()
        df['vol_1t_sum_last_17w'] = df.volume.rolling(daily_count * 5 * 17).sum()
        df['vol_1t_sum_last_18w'] = df.volume.rolling(daily_count * 5 * 18).sum()
        df['vol_1t_sum_last_19w'] = df.volume.rolling(daily_count * 5 * 19).sum()
        df['vol_1t_sum_last_20w'] = df.volume.rolling(daily_count * 5 * 20).sum()
        df['vol_1t_sum_last_21w'] = df.volume.rolling(daily_count * 5 * 21).sum()
        df['vol_1t_sum_last_22w'] = df.volume.rolling(daily_count * 5 * 22).sum()
        df['vol_1t_sum_last_23w'] = df.volume.rolling(daily_count * 5 * 23).sum()
        df['vol_1t_sum_last_24w'] = df.volume.rolling(daily_count * 5 * 24).sum()
        df['vol_1t_sum_last_25w'] = df.volume.rolling(daily_count * 5 * 25).sum()
        df['vol_1t_sum_last_26w'] = df.volume.rolling(daily_count * 5 * 26).sum()
        df['vol_1t_sum_last_27w'] = df.volume.rolling(daily_count * 5 * 27).sum()
        df['vol_1t_sum_last_28w'] = df.volume.rolling(daily_count * 5 * 28).sum()
        df['vol_1t_sum_last_29w'] = df.volume.rolling(daily_count * 5 * 29).sum()
        df['vol_1t_sum_last_30w'] = df.volume.rolling(daily_count * 5 * 30).sum()
        df['vol_1t_sum_last_31w'] = df.volume.rolling(daily_count * 5 * 31).sum()
        df['vol_1t_sum_last_32w'] = df.volume.rolling(daily_count * 5 * 32).sum()
        df['vol_1t_sum_last_33w'] = df.volume.rolling(daily_count * 5 * 33).sum()
        df['vol_1t_sum_last_34w'] = df.volume.rolling(daily_count * 5 * 34).sum()
        df['vol_1t_sum_last_35w'] = df.volume.rolling(daily_count * 5 * 35).sum()
        df['vol_1t_sum_last_36w'] = df.volume.rolling(daily_count * 5 * 36).sum()
        df['vol_1t_sum_last_37w'] = df.volume.rolling(daily_count * 5 * 37).sum()
        df['vol_1t_sum_last_38w'] = df.volume.rolling(daily_count * 5 * 38).sum()
        df['vol_1t_sum_last_39w'] = df.volume.rolling(daily_count * 5 * 39).sum()
        df['vol_1t_sum_last_40w'] = df.volume.rolling(daily_count * 5 * 40).sum()
        df['vol_1t_sum_last_41w'] = df.volume.rolling(daily_count * 5 * 41).sum()
        df['vol_1t_sum_last_42w'] = df.volume.rolling(daily_count * 5 * 42).sum()
        df['vol_1t_sum_last_43w'] = df.volume.rolling(daily_count * 5 * 43).sum()
        df['vol_1t_sum_last_44w'] = df.volume.rolling(daily_count * 5 * 44).sum()
        df['vol_1t_sum_last_45w'] = df.volume.rolling(daily_count * 5 * 45).sum()
        df['vol_1t_sum_last_46w'] = df.volume.rolling(daily_count * 5 * 46).sum()
        df['vol_1t_sum_last_47w'] = df.volume.rolling(daily_count * 5 * 47).sum()
        df['vol_1t_sum_last_48w'] = df.volume.rolling(daily_count * 5 * 48).sum()

        return df

    @staticmethod
    def add_close_vol_ma(df, daily_count):
        df['closema_01d'] = talib.MA(df.close, timeperiod=daily_count * 1)
        df['closema_02d'] = talib.MA(df.close, timeperiod=daily_count * 2)
        df['closema_03d'] = talib.MA(df.close, timeperiod=daily_count * 3)
        df['closema_04d'] = talib.MA(df.close, timeperiod=daily_count * 4)
        df['closema_01w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  1)
        df['closema_02w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  2)
        df['closema_03w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  3)
        df['closema_04w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  4)
        df['closema_05w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  5)
        df['closema_06w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  6)
        df['closema_07w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  7)
        df['closema_08w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  8)
        df['closema_09w'] = talib.MA(df.close, timeperiod=daily_count * 5 *  9)
        df['closema_10w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 10)
        df['closema_11w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 11)
        df['closema_12w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 12)
        df['closema_13w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 13)
        df['closema_14w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 14)
        df['closema_15w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 15)
        df['closema_16w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 16)
        df['closema_17w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 17)
        df['closema_18w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 18)
        df['closema_19w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 19)
        df['closema_20w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 20)
        df['closema_21w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 21)
        df['closema_22w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 22)
        df['closema_23w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 23)
        df['closema_24w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 24)
        df['closema_25w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 25)
        df['closema_26w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 26)
        df['closema_27w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 27)
        df['closema_28w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 28)
        df['closema_29w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 29)
        df['closema_30w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 30)
        df['closema_31w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 31)
        df['closema_32w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 32)
        df['closema_33w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 33)
        df['closema_34w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 34)
        df['closema_35w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 35)
        df['closema_36w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 36)
        df['closema_37w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 37)
        df['closema_38w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 38)
        df['closema_39w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 39)
        df['closema_40w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 40)
        df['closema_41w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 41)
        df['closema_42w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 42)
        df['closema_43w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 43)
        df['closema_44w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 44)
        df['closema_45w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 45)
        df['closema_46w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 46)
        df['closema_47w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 47)
        df['closema_48w'] = talib.MA(df.close, timeperiod=daily_count * 5 * 48)

        df['volma_01d'] = talib.MA(df.volume, timeperiod=daily_count * 1)
        df['volma_02d'] = talib.MA(df.volume, timeperiod=daily_count * 2)
        df['volma_03d'] = talib.MA(df.volume, timeperiod=daily_count * 3)
        df['volma_04d'] = talib.MA(df.volume, timeperiod=daily_count * 4)
        df['volma_01w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  1)
        df['volma_02w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  2)
        df['volma_03w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  3)
        df['volma_04w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  4)
        df['volma_05w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  5)
        df['volma_06w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  6)
        df['volma_07w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  7)
        df['volma_08w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  8)
        df['volma_09w'] = talib.MA(df.volume, timeperiod=daily_count * 5 *  9)
        df['volma_10w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 10)
        df['volma_11w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 11)
        df['volma_12w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 12)
        df['volma_13w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 13)
        df['volma_14w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 14)
        df['volma_15w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 15)
        df['volma_16w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 16)
        df['volma_17w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 17)
        df['volma_18w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 18)
        df['volma_19w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 19)
        df['volma_20w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 20)
        df['volma_21w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 21)
        df['volma_22w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 22)
        df['volma_23w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 23)
        df['volma_24w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 24)
        df['volma_25w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 25)
        df['volma_26w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 26)
        df['volma_27w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 27)
        df['volma_28w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 28)
        df['volma_29w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 29)
        df['volma_30w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 30)
        df['volma_31w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 31)
        df['volma_32w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 32)
        df['volma_33w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 33)
        df['volma_34w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 34)
        df['volma_35w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 35)
        df['volma_36w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 36)
        df['volma_37w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 37)
        df['volma_38w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 38)
        df['volma_39w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 39)
        df['volma_40w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 40)
        df['volma_41w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 41)
        df['volma_42w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 42)
        df['volma_43w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 43)
        df['volma_44w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 44)
        df['volma_45w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 45)
        df['volma_46w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 46)
        df['volma_47w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 47)
        df['volma_48w'] = talib.MA(df.volume, timeperiod=daily_count * 5 * 48)
        
        return df
        
        
    @staticmethod
    def add_closema_indicators(df, daily_count):
        factor_4w = daily_count * 20
        factor_3w = daily_count * 15
        factor_2w = daily_count * 10
        factor_5d = daily_count * 5
        factor_4d = daily_count * 4
        factor_3d = daily_count * 3
        factor_2d = daily_count * 2
        factor_1d = daily_count * 1
        factor_1h = int(daily_count/4)

        df['closema_4w'] = talib.MA(df.close, timeperiod=factor_4w)
        df['closema_3w'] = talib.MA(df.close, timeperiod=factor_3w)
        df['closema_2w'] = talib.MA(df.close, timeperiod=factor_2w)
        df['closema_5d'] = talib.MA(df.close, timeperiod=factor_5d)
        df['closema_4d'] = talib.MA(df.close, timeperiod=factor_4d)
        df['closema_3d'] = talib.MA(df.close, timeperiod=factor_3d)
        df['closema_2d'] = talib.MA(df.close, timeperiod=factor_2d)
        df['closema_1d'] = talib.MA(df.close, timeperiod=factor_1d)
        df['closema_1h'] = talib.MA(df.close, timeperiod=factor_1h)
        
        df['closema_avg'] = (df.closema_1h + df.closema_1d*4 + df.closema_2d*8 + df.closema_3d*12 + df.closema_4d*16 + df.closema_5d*20 + df.closema_2w*40 + df.closema_3w*60 + df.closema_4w*80) / (1+4+8+12+16+20+40+60+80)
        
        return df

    @staticmethod
    def add_rsi_indicators(df, daily_count):
        factor_4w = daily_count * 20
        factor_3w = daily_count * 15
        factor_2w = daily_count * 10
        factor_5d = daily_count * 5
        factor_4d = daily_count * 4
        factor_3d = daily_count * 3
        factor_2d = daily_count * 2
        factor_1d = daily_count * 1
        factor_1h = int(daily_count/4)

        df['rsi_4w'] = talib.RSI(df.close, timeperiod=factor_4w)
        df['rsi_3w'] = talib.RSI(df.close, timeperiod=factor_3w)
        df['rsi_2w'] = talib.RSI(df.close, timeperiod=factor_2w)
        df['rsi_5d'] = talib.RSI(df.close, timeperiod=factor_5d)
        df['rsi_4d'] = talib.RSI(df.close, timeperiod=factor_4d)
        df['rsi_3d'] = talib.RSI(df.close, timeperiod=factor_3d)
        df['rsi_2d'] = talib.RSI(df.close, timeperiod=factor_2d)
        df['rsi_1d'] = talib.RSI(df.close, timeperiod=factor_1d)
        df['rsi_1h'] = talib.RSI(df.close, timeperiod=factor_1h)
        
        return df

    @staticmethod
    def add_macd_indicators(df, daily_count):
        factor_00d = int(daily_count/4)
        factor_01d = daily_count * 1
        factor_02d = daily_count * 2
        factor_03d = daily_count * 3
        factor_04d = daily_count * 4
        factor_05d = daily_count * 5
        factor_06d = daily_count * 6
        factor_07d = daily_count * 7
        factor_08d = daily_count * 8
        factor_09d = daily_count * 9
        factor_10d = daily_count * 10
        factor_11d = daily_count * 11
        factor_12d = daily_count * 12
        factor_13d = daily_count * 13
        factor_14d = daily_count * 14
        factor_15d = daily_count * 15
        factor_16d = daily_count * 16
        factor_17d = daily_count * 17
        factor_18d = daily_count * 18
        factor_19d = daily_count * 19
        factor_20d = daily_count * 20
        factor_21d = daily_count * 21
        factor_22d = daily_count * 22
        factor_23d = daily_count * 23
        factor_24d = daily_count * 24
        factor_25d = daily_count * 25
        factor_26d = daily_count * 26
        factor_27d = daily_count * 27
        factor_28d = daily_count * 28
        factor_29d = daily_count * 29
        factor_30d = daily_count * 30

        # factor_3h = int(3 * daily_count/4)
        # factor_2h = int(daily_count/2)
        # factor_1h = int(daily_count/4)
        # factor_hh = int(daily_count/8)
        # factor_1t = 1
        
        # df['macd_1t'], df['macdsignal_1t'], df['macdhist_1t'] = talib.MACD(df.close, fastperiod=12*factor_1t, slowperiod=26*factor_1t, signalperiod=9*factor_1t)
        # df['macd_hh'], df['macdsignal_hh'], df['macdhist_hh'] = talib.MACD(df.close, fastperiod=12*factor_hh, slowperiod=26*factor_hh, signalperiod=9*factor_hh)
        # df['macd_1h'], df['macdsignal_1h'], df['macdhist_1h'] = talib.MACD(df.close, fastperiod=12*factor_1h, slowperiod=26*factor_1h, signalperiod=9*factor_1h)
        # df['macd_2h'], df['macdsignal_2h'], df['macdhist_2h'] = talib.MACD(df.close, fastperiod=12*factor_2h, slowperiod=26*factor_2h, signalperiod=9*factor_2h)
        # df['macd_00d'], df['macdsignal_00d'], df['macdhist_00d'] = talib.MACD(df.close, fastperiod=12*factor_00d, slowperiod=26*factor_00d, signalperiod=9*factor_00d)
        df['macd_01d'], df['macdsignal_01d'], df['macdhist_01d'] = talib.MACD(df.close, fastperiod=12*factor_01d, slowperiod=26*factor_01d, signalperiod=9*factor_01d)
        df['macd_02d'], df['macdsignal_02d'], df['macdhist_02d'] = talib.MACD(df.close, fastperiod=12*factor_02d, slowperiod=26*factor_02d, signalperiod=9*factor_02d)
        df['macd_03d'], df['macdsignal_03d'], df['macdhist_03d'] = talib.MACD(df.close, fastperiod=12*factor_03d, slowperiod=26*factor_03d, signalperiod=9*factor_03d)
        df['macd_04d'], df['macdsignal_04d'], df['macdhist_04d'] = talib.MACD(df.close, fastperiod=12*factor_04d, slowperiod=26*factor_04d, signalperiod=9*factor_04d)
        df['macd_05d'], df['macdsignal_05d'], df['macdhist_05d'] = talib.MACD(df.close, fastperiod=12*factor_05d, slowperiod=26*factor_05d, signalperiod=9*factor_05d)
        df['macd_06d'], df['macdsignal_06d'], df['macdhist_06d'] = talib.MACD(df.close, fastperiod=12*factor_06d, slowperiod=26*factor_06d, signalperiod=9*factor_06d)
        df['macd_07d'], df['macdsignal_07d'], df['macdhist_07d'] = talib.MACD(df.close, fastperiod=12*factor_07d, slowperiod=26*factor_07d, signalperiod=9*factor_07d)
        df['macd_08d'], df['macdsignal_08d'], df['macdhist_08d'] = talib.MACD(df.close, fastperiod=12*factor_08d, slowperiod=26*factor_08d, signalperiod=9*factor_08d)
        df['macd_09d'], df['macdsignal_09d'], df['macdhist_09d'] = talib.MACD(df.close, fastperiod=12*factor_09d, slowperiod=26*factor_09d, signalperiod=9*factor_09d)
        df['macd_10d'], df['macdsignal_10d'], df['macdhist_10d'] = talib.MACD(df.close, fastperiod=12*factor_10d, slowperiod=26*factor_10d, signalperiod=9*factor_10d)
        df['macd_11d'], df['macdsignal_11d'], df['macdhist_11d'] = talib.MACD(df.close, fastperiod=12*factor_11d, slowperiod=26*factor_11d, signalperiod=9*factor_11d)
        df['macd_12d'], df['macdsignal_12d'], df['macdhist_12d'] = talib.MACD(df.close, fastperiod=12*factor_12d, slowperiod=26*factor_12d, signalperiod=9*factor_12d)
        df['macd_13d'], df['macdsignal_13d'], df['macdhist_13d'] = talib.MACD(df.close, fastperiod=12*factor_13d, slowperiod=26*factor_13d, signalperiod=9*factor_13d)
        df['macd_14d'], df['macdsignal_14d'], df['macdhist_14d'] = talib.MACD(df.close, fastperiod=12*factor_14d, slowperiod=26*factor_14d, signalperiod=9*factor_14d)
        df['macd_15d'], df['macdsignal_15d'], df['macdhist_15d'] = talib.MACD(df.close, fastperiod=12*factor_15d, slowperiod=26*factor_15d, signalperiod=9*factor_15d)
        df['macd_16d'], df['macdsignal_16d'], df['macdhist_16d'] = talib.MACD(df.close, fastperiod=12*factor_16d, slowperiod=26*factor_16d, signalperiod=9*factor_16d)
        df['macd_17d'], df['macdsignal_17d'], df['macdhist_17d'] = talib.MACD(df.close, fastperiod=12*factor_17d, slowperiod=26*factor_17d, signalperiod=9*factor_17d)
        df['macd_18d'], df['macdsignal_18d'], df['macdhist_18d'] = talib.MACD(df.close, fastperiod=12*factor_18d, slowperiod=26*factor_18d, signalperiod=9*factor_18d)
        df['macd_19d'], df['macdsignal_19d'], df['macdhist_19d'] = talib.MACD(df.close, fastperiod=12*factor_19d, slowperiod=26*factor_19d, signalperiod=9*factor_19d)
        df['macd_20d'], df['macdsignal_20d'], df['macdhist_20d'] = talib.MACD(df.close, fastperiod=12*factor_20d, slowperiod=26*factor_20d, signalperiod=9*factor_20d)
        # df['macd_21d'], df['macdsignal_21d'], df['macdhist_21d'] = talib.MACD(df.close, fastperiod=12*factor_21d, slowperiod=26*factor_21d, signalperiod=9*factor_21d)
        # df['macd_22d'], df['macdsignal_22d'], df['macdhist_22d'] = talib.MACD(df.close, fastperiod=12*factor_22d, slowperiod=26*factor_22d, signalperiod=9*factor_22d)
        # df['macd_23d'], df['macdsignal_23d'], df['macdhist_23d'] = talib.MACD(df.close, fastperiod=12*factor_23d, slowperiod=26*factor_23d, signalperiod=9*factor_23d)
        # df['macd_24d'], df['macdsignal_24d'], df['macdhist_24d'] = talib.MACD(df.close, fastperiod=12*factor_24d, slowperiod=26*factor_24d, signalperiod=9*factor_24d)
        # df['macd_25d'], df['macdsignal_25d'], df['macdhist_25d'] = talib.MACD(df.close, fastperiod=12*factor_25d, slowperiod=26*factor_25d, signalperiod=9*factor_25d)
        # df['macd_26d'], df['macdsignal_26d'], df['macdhist_26d'] = talib.MACD(df.close, fastperiod=12*factor_26d, slowperiod=26*factor_26d, signalperiod=9*factor_26d)
        # df['macd_27d'], df['macdsignal_27d'], df['macdhist_27d'] = talib.MACD(df.close, fastperiod=12*factor_27d, slowperiod=26*factor_27d, signalperiod=9*factor_27d)
        # df['macd_28d'], df['macdsignal_28d'], df['macdhist_28d'] = talib.MACD(df.close, fastperiod=12*factor_28d, slowperiod=26*factor_28d, signalperiod=9*factor_28d)
        # df['macd_29d'], df['macdsignal_29d'], df['macdhist_29d'] = talib.MACD(df.close, fastperiod=12*factor_29d, slowperiod=26*factor_29d, signalperiod=9*factor_29d)
        # df['macd_30d'], df['macdsignal_30d'], df['macdhist_30d'] = talib.MACD(df.close, fastperiod=12*factor_30d, slowperiod=26*factor_30d, signalperiod=9*factor_30d)
        
        df['macdhist_sum'] = 0
        for col in df.columns:
            if col.startswith('macdhist_') and col.endswith('d'):
                df['macdhist_sum'] += df[col]
        df['macdhist_sum'] /= 20
        
        
        # df['macdhist_avg_w'] = (df.macdhist_1w + df.macdhist_2w + df.macdhist_3w + df.macdhist_4w) / 4
        # df['macdhist_avg_d'] = (df.macdhist_1d + df.macdhist_2d + df.macdhist_3d + df.macdhist_4d) / 4
        # df['macdhist_avg_h'] = (df.macdhist_hh + df.macdhist_1h + df.macdhist_2h) / 4

        # df['macdhist_1t_sum_last_0hh'] = df.macdhist_1t.rolling(factor_hh).sum()
        # df['macdhist_1t_sum_last_01h'] = df.macdhist_1t.rolling(factor_1h).sum()
        # df['macdhist_1t_sum_last_02h'] = df.macdhist_1t.rolling(factor_2h).sum()
        # df['macdhist_1t_sum_last_03h'] = df.macdhist_1t.rolling(factor_3h).sum()
        # df['macdhist_1t_sum_last_01d'] = df.macdhist_1t.rolling(daily_count * 1).sum()
        # df['macdhist_1t_sum_last_02d'] = df.macdhist_1t.rolling(daily_count * 2).sum()
        # df['macdhist_1t_sum_last_03d'] = df.macdhist_1t.rolling(daily_count * 3).sum()
        # df['macdhist_1t_sum_last_04d'] = df.macdhist_1t.rolling(daily_count * 4).sum()
        # df['macdhist_1t_sum_last_01w'] = df.macdhist_1t.rolling(daily_count * 5 *  1).sum()
        # df['macdhist_1t_sum_last_02w'] = df.macdhist_1t.rolling(daily_count * 5 *  2).sum()
        # df['macdhist_1t_sum_last_03w'] = df.macdhist_1t.rolling(daily_count * 5 *  3).sum()
        # df['macdhist_1t_sum_last_04w'] = df.macdhist_1t.rolling(daily_count * 5 *  4).sum()
        # df['macdhist_1t_sum_last_05w'] = df.macdhist_1t.rolling(daily_count * 5 *  5).sum()
        # df['macdhist_1t_sum_last_06w'] = df.macdhist_1t.rolling(daily_count * 5 *  6).sum()
        # df['macdhist_1t_sum_last_07w'] = df.macdhist_1t.rolling(daily_count * 5 *  7).sum()
        # df['macdhist_1t_sum_last_08w'] = df.macdhist_1t.rolling(daily_count * 5 *  8).sum()
        # df['macdhist_1t_sum_last_09w'] = df.macdhist_1t.rolling(daily_count * 5 *  9).sum()
        # df['macdhist_1t_sum_last_10w'] = df.macdhist_1t.rolling(daily_count * 5 * 10).sum()
        # df['macdhist_1t_sum_last_11w'] = df.macdhist_1t.rolling(daily_count * 5 * 11).sum()
        # df['macdhist_1t_sum_last_12w'] = df.macdhist_1t.rolling(daily_count * 5 * 12).sum()
        # df['macdhist_1t_sum_last_13w'] = df.macdhist_1t.rolling(daily_count * 5 * 13).sum()
        # df['macdhist_1t_sum_last_14w'] = df.macdhist_1t.rolling(daily_count * 5 * 14).sum()
        # df['macdhist_1t_sum_last_15w'] = df.macdhist_1t.rolling(daily_count * 5 * 15).sum()
        # df['macdhist_1t_sum_last_16w'] = df.macdhist_1t.rolling(daily_count * 5 * 16).sum()
        # df['macdhist_1t_sum_last_17w'] = df.macdhist_1t.rolling(daily_count * 5 * 17).sum()
        # df['macdhist_1t_sum_last_18w'] = df.macdhist_1t.rolling(daily_count * 5 * 18).sum()
        # df['macdhist_1t_sum_last_19w'] = df.macdhist_1t.rolling(daily_count * 5 * 19).sum()
        # df['macdhist_1t_sum_last_20w'] = df.macdhist_1t.rolling(daily_count * 5 * 20).sum()
        # df['macdhist_1t_sum_last_21w'] = df.macdhist_1t.rolling(daily_count * 5 * 21).sum()
        # df['macdhist_1t_sum_last_22w'] = df.macdhist_1t.rolling(daily_count * 5 * 22).sum()
        # df['macdhist_1t_sum_last_23w'] = df.macdhist_1t.rolling(daily_count * 5 * 23).sum()
        # df['macdhist_1t_sum_last_24w'] = df.macdhist_1t.rolling(daily_count * 5 * 24).sum()

        return df