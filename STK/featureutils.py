#coding=utf-8

import numpy as np
import pandas as pd
import talib
from scipy import stats
from datagent import BaosAgent


class FeatureTool:

    @staticmethod
    def get_slope(x):
        lgr = stats.linregress(range(0, len(x)), x)
        return lgr.slope

    @staticmethod
    def add_bband_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_upper  = 'BAND_upper_' + str(idx)
            col_middle = 'BAND_middle_' + str(idx)
            col_lower  = 'BAND_lower_' + str(idx)
            df[col_upper], df[col_middle], df[col_lower] = talib.BBANDS(df.close, timeperiod=daily_count * idx, nbdevup=2, nbdevdn=2, matype=0)

        return df

    @staticmethod
    def add_atr_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'ATR_' + str(idx)
            df[col_name] = talib.ATR(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df
    
    @staticmethod
    def add_mfi_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'MFI_' + str(idx)
            df[col_name] = talib.MFI(df.high, df.low, df.close, df.volume, timeperiod=daily_count * idx)
        
        mfi_sum = pd.Series(data=np.zeros((len(df))))
        for col in df.columns:
            if col.startswith('MFI_'):
                mfi_sum += df[col]
        df['MFISUM_AVG'] = mfi_sum / count
        

        return df
    
    @staticmethod
    def add_rsi_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'RSI_' + str(idx)
            df[col_name] = talib.RSI(df.close, timeperiod=daily_count * idx)
        return df
    
    @staticmethod
    def add_adx_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'ADX_' + str(idx)
            df[col_name] = talib.ADX(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df
    
    @staticmethod
    def add_plusdi_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'PLUSDI_' + str(idx)
            df[col_name] = talib.PLUS_DI(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df
    
    @staticmethod
    def add_minusdi_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'MINUSDI_' + str(idx)
            df[col_name] = talib.MINUS_DI(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df

    @staticmethod
    def add_kd_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name_a = 'K_' + str(idx)
            col_name_b = 'D_' + str(idx)
            df[col_name_a], df[col_name_b] = talib.STOCH(df.high, df.low, df.close, fastk_period=daily_count * idx , slowk_period=daily_count * idx , slowk_matype=0,slowd_period=daily_count * idx , slowd_matype=0)
        k_sum = pd.Series(data=np.zeros((len(df))))
        for col in df.columns:
            if col.startswith('K_'):
                k_sum += df[col]
        df['KSUM_AVG'] = k_sum / count
        return df

    @staticmethod
    def add_cci_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'CCI_' + str(idx)
            df[col_name] = talib.MINUS_DI(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df

    @staticmethod
    def add_dx_ft(df, daily_count, count):
        for idx in range(1, count + 1):
            col_name = 'DX_' + str(idx)
            df[col_name] = talib.DX(df.high, df.low, df.close, timeperiod=daily_count * idx)
        return df

    @staticmethod
    def add_ta_features(df, daily_count):
        df = FeatureTool.add_mfi_ft(df, daily_count, 20)
        df = FeatureTool.add_rsi_ft(df, daily_count, 20)
        df = FeatureTool.add_atr_ft(df, daily_count, 20)
        # df = FeatureTool.add_cci_ft(df, daily_count, 60)
        # df = FeatureTool.add_adx_ft(df, daily_count, 60)
        df = FeatureTool.add_plusdi_ft(df, daily_count, 20)
        df = FeatureTool.add_minusdi_ft(df, daily_count, 20)
        # df = FeatureTool.add_dx_ft(df, daily_count, 60)
        df = FeatureTool.add_bband_ft(df, daily_count, 20)
        df = FeatureTool.add_kd_ft(df, daily_count, 30)
        df['k_avg_01'] = (df.K_1+df.K_2+df.K_3+df.K_4+df.K_5)/5
        df['k_avg_02'] = (df.K_6+df.K_7+df.K_8+df.K_9+df.K_10)/5
        df['k_avg_03'] = (df.K_11+df.K_12+df.K_13+df.K_14+df.K_15)/5
        df['k_avg_04'] = (df.K_16+df.K_17+df.K_18+df.K_19+df.K_20)/5
        df['k_avg_05'] = (df.K_21+df.K_22+df.K_23+df.K_24+df.K_25)/5
        df['k_avg_06'] = (df.K_26+df.K_27+df.K_28+df.K_29+df.K_30)/5
        # df['k_avg_07'] = (df.K_31+df.K_32+df.K_33+df.K_34+df.K_35)/5
        # df['k_avg_08'] = (df.K_36+df.K_37+df.K_38+df.K_39+df.K_40)/5
        # df['k_avg_09'] = (df.K_41+df.K_42+df.K_43+df.K_44+df.K_45)/5
        # df['k_avg_10'] = (df.K_46+df.K_47+df.K_48+df.K_49+df.K_50)/5
        # df['k_avg_11'] = (df.K_51+df.K_12+df.K_53+df.K_54+df.K_55)/5
        # df['k_avg_12'] = (df.K_56+df.K_57+df.K_58+df.K_59+df.K_60)/5
        # df['k_avg_13'] = (df.K_61+df.K_12+df.K_63+df.K_64+df.K_65)/5
        # df['k_avg_14'] = (df.K_66+df.K_67+df.K_68+df.K_69+df.K_70)/5
        # df['k_avg_15'] = (df.K_71+df.K_12+df.K_73+df.K_74+df.K_75)/5
        # df['k_avg_16'] = (df.K_76+df.K_77+df.K_78+df.K_79+df.K_80)/5
        # df['k_avg_17'] = (df.K_81+df.K_12+df.K_83+df.K_84+df.K_85)/5
        # df['k_avg_18'] = (df.K_86+df.K_87+df.K_88+df.K_89+df.K_90)/5

        # df['macd'], df['macdsignal'], df['macdhist'] = talib.MACD(df.close, fastperiod=12 * daily_count, slowperiod=26 * daily_count, signalperiod=9 * daily_count)
        # df['obv'] = talib.OBV(df.close, df.volume)
        # df['ad']  = talib.AD(df.high, df.low, df.close, df.volume)
        # df['bop'] = talib.BOP(df.open, df.high, df.low, df.close)
        df['slope_KSUM_AVG'] = df.KSUM_AVG.rolling(daily_count * 5).apply(lambda x:FeatureTool.get_slope(x), raw=True)
        df['slope_close'] = df.close.rolling(daily_count * 5).apply(lambda x:FeatureTool.get_slope(x), raw=True)
        df['slope_MFISUM_AVG'] = df.MFISUM_AVG.rolling(daily_count * 5).apply(lambda x:FeatureTool.get_slope(x), raw=True)
        return df
    
    @staticmethod
    def add_close_features(df, daily_count):
        df['close_ema_01d']  = talib.EMA(df.close, timeperiod=daily_count*1*1)
        df['close_ema_02d']  = talib.EMA(df.close, timeperiod=daily_count*1*2)
        df['close_ema_03d']  = talib.EMA(df.close, timeperiod=daily_count*1*3)
        df['close_ema_04d']  = talib.EMA(df.close, timeperiod=daily_count*1*4)
        
        df['close_ma_01d']  = talib.MA(df.close, timeperiod=daily_count*1*1)
        df['close_ma_02d']  = talib.MA(df.close, timeperiod=daily_count*1*2)
        df['close_ma_03d']  = talib.MA(df.close, timeperiod=daily_count*1*3)
        df['close_ma_04d']  = talib.MA(df.close, timeperiod=daily_count*1*4)
        
        df['close_sma_01d']  = talib.SMA(df.close, timeperiod=daily_count*1*1)
        df['close_sma_02d']  = talib.SMA(df.close, timeperiod=daily_count*1*2)
        df['close_sma_03d']  = talib.SMA(df.close, timeperiod=daily_count*1*3)
        df['close_sma_04d']  = talib.SMA(df.close, timeperiod=daily_count*1*4)
        
        df['close_avg_01d'] = (df.close_ema_01d + df.close_ma_01d + df.close_sma_01d)/3
        df['close_avg_02d'] = (df.close_ema_02d + df.close_ma_02d + df.close_sma_02d)/3
        df['close_avg_03d'] = (df.close_ema_03d + df.close_ma_03d + df.close_sma_03d)/3
        df['close_avg_04d'] = (df.close_ema_04d + df.close_ma_04d + df.close_sma_04d)/3
        
        # df['close_ud'] = 100 * (df.close - df.close.shift(1)) / df.close.shift(1)
        # df['close_avg_01d_ud'] = 100 * (df.close_avg_01d - df.close_avg_01d.shift(1)) / df.close_avg_01d.shift(1)
        
        df['close_ema_01w']  = talib.EMA(df.close, timeperiod=daily_count*5*1)
        df['close_ema_02w']  = talib.EMA(df.close, timeperiod=daily_count*5*2)
        df['close_ema_03w']  = talib.EMA(df.close, timeperiod=daily_count*5*3)
        df['close_ema_04w']  = talib.EMA(df.close, timeperiod=daily_count*5*4)
        df['close_ema_05w']  = talib.EMA(df.close, timeperiod=daily_count*5*5)
        df['close_ema_06w']  = talib.EMA(df.close, timeperiod=daily_count*5*6)
        df['close_ema_07w']  = talib.EMA(df.close, timeperiod=daily_count*5*7)
        df['close_ema_08w']  = talib.EMA(df.close, timeperiod=daily_count*5*8)
        df['close_ema_09w']  = talib.EMA(df.close, timeperiod=daily_count*5*9)
        df['close_ema_10w']  = talib.EMA(df.close, timeperiod=daily_count*5*10)
        df['close_ema_11w']  = talib.EMA(df.close, timeperiod=daily_count*5*11)
        df['close_ema_12w']  = talib.EMA(df.close, timeperiod=daily_count*5*12)
        df['close_ema_13w']  = talib.EMA(df.close, timeperiod=daily_count*5*13)
        df['close_ema_14w']  = talib.EMA(df.close, timeperiod=daily_count*5*14)
        df['close_ema_15w']  = talib.EMA(df.close, timeperiod=daily_count*5*15)
        df['close_ema_16w']  = talib.EMA(df.close, timeperiod=daily_count*5*16)
        df['close_ema_17w']  = talib.EMA(df.close, timeperiod=daily_count*5*17)
        df['close_ema_18w']  = talib.EMA(df.close, timeperiod=daily_count*5*18)
        df['close_ema_19w']  = talib.EMA(df.close, timeperiod=daily_count*5*19)
        df['close_ema_20w']  = talib.EMA(df.close, timeperiod=daily_count*5*20)
        
        df['close_ma_01w']  = talib.MA(df.close, timeperiod=daily_count*5*1)
        df['close_ma_02w']  = talib.MA(df.close, timeperiod=daily_count*5*2)
        df['close_ma_03w']  = talib.MA(df.close, timeperiod=daily_count*5*3)
        df['close_ma_04w']  = talib.MA(df.close, timeperiod=daily_count*5*4)
        df['close_ma_05w']  = talib.MA(df.close, timeperiod=daily_count*5*5)
        df['close_ma_06w']  = talib.MA(df.close, timeperiod=daily_count*5*6)
        df['close_ma_07w']  = talib.MA(df.close, timeperiod=daily_count*5*7)
        df['close_ma_08w']  = talib.MA(df.close, timeperiod=daily_count*5*8)
        df['close_ma_09w']  = talib.MA(df.close, timeperiod=daily_count*5*9)
        df['close_ma_10w']  = talib.MA(df.close, timeperiod=daily_count*5*10)
        df['close_ma_11w']  = talib.MA(df.close, timeperiod=daily_count*5*11)
        df['close_ma_12w']  = talib.MA(df.close, timeperiod=daily_count*5*12)
        df['close_ma_13w']  = talib.MA(df.close, timeperiod=daily_count*5*13)
        df['close_ma_14w']  = talib.MA(df.close, timeperiod=daily_count*5*14)
        df['close_ma_15w']  = talib.MA(df.close, timeperiod=daily_count*5*15)
        df['close_ma_16w']  = talib.MA(df.close, timeperiod=daily_count*5*16)
        df['close_ma_17w']  = talib.MA(df.close, timeperiod=daily_count*5*17)
        df['close_ma_18w']  = talib.MA(df.close, timeperiod=daily_count*5*18)
        df['close_ma_19w']  = talib.MA(df.close, timeperiod=daily_count*5*19)
        df['close_ma_20w']  = talib.MA(df.close, timeperiod=daily_count*5*20)
        
        df['close_sma_01w']  = talib.SMA(df.close, timeperiod=daily_count*5*1)
        df['close_sma_02w']  = talib.SMA(df.close, timeperiod=daily_count*5*2)
        df['close_sma_03w']  = talib.SMA(df.close, timeperiod=daily_count*5*3)
        df['close_sma_04w']  = talib.SMA(df.close, timeperiod=daily_count*5*4)
        df['close_sma_05w']  = talib.SMA(df.close, timeperiod=daily_count*5*5)
        df['close_sma_06w']  = talib.SMA(df.close, timeperiod=daily_count*5*6)
        df['close_sma_07w']  = talib.SMA(df.close, timeperiod=daily_count*5*7)
        df['close_sma_08w']  = talib.SMA(df.close, timeperiod=daily_count*5*8)
        df['close_sma_09w']  = talib.SMA(df.close, timeperiod=daily_count*5*9)
        df['close_sma_10w']  = talib.SMA(df.close, timeperiod=daily_count*5*10)
        df['close_sma_11w']  = talib.SMA(df.close, timeperiod=daily_count*5*11)
        df['close_sma_12w']  = talib.SMA(df.close, timeperiod=daily_count*5*12)
        df['close_sma_13w']  = talib.SMA(df.close, timeperiod=daily_count*5*13)
        df['close_sma_14w']  = talib.SMA(df.close, timeperiod=daily_count*5*14)
        df['close_sma_15w']  = talib.SMA(df.close, timeperiod=daily_count*5*15)
        df['close_sma_16w']  = talib.SMA(df.close, timeperiod=daily_count*5*16)
        df['close_sma_17w']  = talib.SMA(df.close, timeperiod=daily_count*5*17)
        df['close_sma_18w']  = talib.SMA(df.close, timeperiod=daily_count*5*18)
        df['close_sma_19w']  = talib.SMA(df.close, timeperiod=daily_count*5*19)
        df['close_sma_20w']  = talib.SMA(df.close, timeperiod=daily_count*5*20)
        
        df['close_avg_01w'] = (df.close_ema_01w + df.close_ma_01w + df.close_sma_01w)/3
        df['close_avg_02w'] = (df.close_ema_02w + df.close_ma_02w + df.close_sma_02w)/3
        df['close_avg_03w'] = (df.close_ema_03w + df.close_ma_03w + df.close_sma_03w)/3
        df['close_avg_04w'] = (df.close_ema_04w + df.close_ma_04w + df.close_sma_04w)/3
        df['close_avg_05w'] = (df.close_ema_05w + df.close_ma_05w + df.close_sma_05w)/3
        df['close_avg_06w'] = (df.close_ema_06w + df.close_ma_06w + df.close_sma_06w)/3
        df['close_avg_07w'] = (df.close_ema_07w + df.close_ma_07w + df.close_sma_07w)/3
        df['close_avg_08w'] = (df.close_ema_08w + df.close_ma_08w + df.close_sma_08w)/3
        df['close_avg_09w'] = (df.close_ema_09w + df.close_ma_09w + df.close_sma_09w)/3
        df['close_avg_10w'] = (df.close_ema_10w + df.close_ma_10w + df.close_sma_10w)/3
        df['close_avg_11w'] = (df.close_ema_11w + df.close_ma_11w + df.close_sma_11w)/3
        df['close_avg_12w'] = (df.close_ema_12w + df.close_ma_12w + df.close_sma_12w)/3
        df['close_avg_13w'] = (df.close_ema_13w + df.close_ma_13w + df.close_sma_13w)/3
        df['close_avg_14w'] = (df.close_ema_14w + df.close_ma_14w + df.close_sma_14w)/3
        df['close_avg_15w'] = (df.close_ema_15w + df.close_ma_15w + df.close_sma_15w)/3
        df['close_avg_16w'] = (df.close_ema_16w + df.close_ma_16w + df.close_sma_16w)/3
        df['close_avg_17w'] = (df.close_ema_17w + df.close_ma_17w + df.close_sma_17w)/3
        df['close_avg_18w'] = (df.close_ema_18w + df.close_ma_18w + df.close_sma_18w)/3
        df['close_avg_19w'] = (df.close_ema_19w + df.close_ma_19w + df.close_sma_19w)/3
        df['close_avg_20w'] = (df.close_ema_20w + df.close_ma_20w + df.close_sma_20w)/3

        # df['close_avg_max'] = df[['close_avg_01w','close_avg_02w','close_avg_03w','close_avg_04w','close_avg_05w','close_avg_06w','close_avg_07w','close_avg_08w','close_avg_09w','close_avg_10w','close_avg_11w','close_avg_12w','close_avg_13w','close_avg_14w','close_avg_15w','close_avg_16w','close_avg_17w','close_avg_18w','close_avg_19w','close_avg_20w']].max(axis=1)
        # df['close_avg_min'] = df[['close_avg_01w','close_avg_02w','close_avg_03w','close_avg_04w','close_avg_05w','close_avg_06w','close_avg_07w','close_avg_08w','close_avg_09w','close_avg_10w','close_avg_11w','close_avg_12w','close_avg_13w','close_avg_14w','close_avg_15w','close_avg_16w','close_avg_17w','close_avg_18w','close_avg_19w','close_avg_20w']].min(axis=1)
        # df['close_avg_range'] = (df.close_avg_max - df.close_avg_min) / df.close_avg_min

        # df['close_avg_01w_diff'] = df.close_avg_01w.diff(1)
        # close_dif_01 = (df.close_avg_01w - df.close_avg_02w)
        # close_dif_02 = (df.close_avg_02w - df.close_avg_03w)
        # close_dif_03 = (df.close_avg_03w - df.close_avg_04w)
        # close_dif_04 = (df.close_avg_04w - df.close_avg_05w)
        # close_dif_05 = (df.close_avg_05w - df.close_avg_06w)
        # close_dif_06 = (df.close_avg_06w - df.close_avg_07w)
        # close_dif_07 = (df.close_avg_07w - df.close_avg_08w)
        # close_dif_08 = (df.close_avg_08w - df.close_avg_09w)
        # close_dif_09 = (df.close_avg_09w - df.close_avg_10w)
        # close_dif_10 = (df.close_avg_10w - df.close_avg_11w)
        # close_dif_11 = (df.close_avg_11w - df.close_avg_12w)
        # close_dif_12 = (df.close_avg_12w - df.close_avg_13w)
        # close_dif_13 = (df.close_avg_13w - df.close_avg_14w)
        # close_dif_14 = (df.close_avg_14w - df.close_avg_15w)
        # close_dif_15 = (df.close_avg_15w - df.close_avg_16w)
        # close_dif_16 = (df.close_avg_16w - df.close_avg_17w)
        # close_dif_17 = (df.close_avg_17w - df.close_avg_18w)
        # close_dif_18 = (df.close_avg_18w - df.close_avg_19w)
        # close_dif_19 = (df.close_avg_19w - df.close_avg_20w)
        # df['close_avg_diff_sum'] = close_dif_01+close_dif_02+close_dif_03+close_dif_04+close_dif_05+close_dif_06+close_dif_07+close_dif_08+close_dif_09+close_dif_10+close_dif_11+close_dif_12+close_dif_13+close_dif_14+close_dif_15+close_dif_16+close_dif_17+close_dif_18+close_dif_19
        # df['close_avg_diff_sum_pre'] = df.close_avg_diff_sum.shift(1)
        

        # df['close_rolling_slope'] = df.close.rolling(slope_windows).apply(func_slope, raw=True)
        # df['close_avg_01w_rolling_slope'] = df.close_avg_01w.rolling(slope_windows).apply(func_slope, raw=True)
        # df['close_avg_02w_rolling_slope'] = df.close_avg_02w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_03w_rolling_slope'] = df.close_avg_03w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_04w_rolling_slope'] = df.close_avg_04w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_05w_rolling_slope'] = df.close_avg_05w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_06w_rolling_slope'] = df.close_avg_06w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_07w_rolling_slope'] = df.close_avg_07w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_08w_rolling_slope'] = df.close_avg_08w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_09w_rolling_slope'] = df.close_avg_09w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_10w_rolling_slope'] = df.close_avg_10w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_11w_rolling_slope'] = df.close_avg_11w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_12w_rolling_slope'] = df.close_avg_12w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_13w_rolling_slope'] = df.close_avg_13w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_14w_rolling_slope'] = df.close_avg_14w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_15w_rolling_slope'] = df.close_avg_15w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_16w_rolling_slope'] = df.close_avg_16w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_17w_rolling_slope'] = df.close_avg_17w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_18w_rolling_slope'] = df.close_avg_18w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_19w_rolling_slope'] = df.close_avg_19w.rolling(5).apply(func_slope, raw=True)
        # df['close_avg_20w_rolling_slope'] = df.close_avg_20w.rolling(5).apply(func_slope, raw=True)
        
        return df

    @staticmethod
    def add_volume_features(df, daily_count):
        df.volume = df.volume / 10000
        # df.volume = np.log10(df.volume)

        df['volume_ema_01d']  = talib.EMA(df.volume, timeperiod=daily_count*1*1)
        df['volume_ema_02d']  = talib.EMA(df.volume, timeperiod=daily_count*1*2)
        df['volume_ema_03d']  = talib.EMA(df.volume, timeperiod=daily_count*1*3)
        df['volume_ema_04d']  = talib.EMA(df.volume, timeperiod=daily_count*1*4)
        df['volume_ema_01w']  = talib.EMA(df.volume, timeperiod=daily_count*5*1)

        df['volume_ma_01d']  = talib.MA(df.volume, timeperiod=daily_count*1*1)
        df['volume_ma_02d']  = talib.MA(df.volume, timeperiod=daily_count*1*2)
        df['volume_ma_03d']  = talib.MA(df.volume, timeperiod=daily_count*1*3)
        df['volume_ma_04d']  = talib.MA(df.volume, timeperiod=daily_count*1*4)
        df['volume_ma_01w']  = talib.MA(df.volume, timeperiod=daily_count*5*1)
        
        df['volume_sma_01d']  = talib.SMA(df.volume, timeperiod=daily_count*1*1)
        df['volume_sma_02d']  = talib.SMA(df.volume, timeperiod=daily_count*1*2)
        df['volume_sma_03d']  = talib.SMA(df.volume, timeperiod=daily_count*1*3)
        df['volume_sma_04d']  = talib.SMA(df.volume, timeperiod=daily_count*1*4)
        df['volume_sma_01w']  = talib.SMA(df.volume, timeperiod=daily_count*5*1)
        
        df['volume_avg_01d'] = (df.volume_ema_01d + df.volume_ma_01d + df.volume_sma_01d)/3
        df['volume_avg_02d'] = (df.volume_ema_02d + df.volume_ma_02d + df.volume_sma_02d)/3
        df['volume_avg_03d'] = (df.volume_ema_03d + df.volume_ma_03d + df.volume_sma_03d)/3
        df['volume_avg_04d'] = (df.volume_ema_04d + df.volume_ma_04d + df.volume_sma_04d)/3
        df['volume_avg_01w'] = (df.volume_ema_01w + df.volume_ma_01w + df.volume_sma_01w)/3

        
        # df['volume_ema_02w']  = talib.EMA(df.volume, timeperiod=daily_count*5*2)
        # df['volume_ema_03w']  = talib.EMA(df.volume, timeperiod=daily_count*5*3)
        # df['volume_ema_04w']  = talib.EMA(df.volume, timeperiod=daily_count*5*4)
        # df['volume_ema_05w']  = talib.EMA(df.volume, timeperiod=daily_count*5*5)
        # df['volume_ema_06w']  = talib.EMA(df.volume, timeperiod=daily_count*5*6)
        # df['volume_ema_07w']  = talib.EMA(df.volume, timeperiod=daily_count*5*7)
        # df['volume_ema_08w']  = talib.EMA(df.volume, timeperiod=daily_count*5*8)
        # df['volume_ema_09w']  = talib.EMA(df.volume, timeperiod=daily_count*5*9)
        # df['volume_ema_10w']  = talib.EMA(df.volume, timeperiod=daily_count*5*10)
        # df['volume_ema_11w']  = talib.EMA(df.volume, timeperiod=daily_count*5*11)
        # df['volume_ema_12w']  = talib.EMA(df.volume, timeperiod=daily_count*5*12)
        # df['volume_ema_13w']  = talib.EMA(df.volume, timeperiod=daily_count*5*13)
        # df['volume_ema_14w']  = talib.EMA(df.volume, timeperiod=daily_count*5*14)
        # df['volume_ema_15w']  = talib.EMA(df.volume, timeperiod=daily_count*5*15)
        # df['volume_ema_16w']  = talib.EMA(df.volume, timeperiod=daily_count*5*16)
        # df['volume_ema_17w']  = talib.EMA(df.volume, timeperiod=daily_count*5*17)
        # df['volume_ema_18w']  = talib.EMA(df.volume, timeperiod=daily_count*5*18)
        # df['volume_ema_19w']  = talib.EMA(df.volume, timeperiod=daily_count*5*19)
        # df['volume_ema_20w']  = talib.EMA(df.volume, timeperiod=daily_count*5*20)
        
        
        # df['volume_ma_02w']  = talib.MA(df.volume, timeperiod=daily_count*5*2)
        # df['volume_ma_03w']  = talib.MA(df.volume, timeperiod=daily_count*5*3)
        # df['volume_ma_04w']  = talib.MA(df.volume, timeperiod=daily_count*5*4)
        # df['volume_ma_05w']  = talib.MA(df.volume, timeperiod=daily_count*5*5)
        # df['volume_ma_06w']  = talib.MA(df.volume, timeperiod=daily_count*5*6)
        # df['volume_ma_07w']  = talib.MA(df.volume, timeperiod=daily_count*5*7)
        # df['volume_ma_08w']  = talib.MA(df.volume, timeperiod=daily_count*5*8)
        # df['volume_ma_09w']  = talib.MA(df.volume, timeperiod=daily_count*5*9)
        # df['volume_ma_10w']  = talib.MA(df.volume, timeperiod=daily_count*5*10)
        # df['volume_ma_11w']  = talib.MA(df.volume, timeperiod=daily_count*5*11)
        # df['volume_ma_12w']  = talib.MA(df.volume, timeperiod=daily_count*5*12)
        # df['volume_ma_13w']  = talib.MA(df.volume, timeperiod=daily_count*5*13)
        # df['volume_ma_14w']  = talib.MA(df.volume, timeperiod=daily_count*5*14)
        # df['volume_ma_15w']  = talib.MA(df.volume, timeperiod=daily_count*5*15)
        # df['volume_ma_16w']  = talib.MA(df.volume, timeperiod=daily_count*5*16)
        # df['volume_ma_17w']  = talib.MA(df.volume, timeperiod=daily_count*5*17)
        # df['volume_ma_18w']  = talib.MA(df.volume, timeperiod=daily_count*5*18)
        # df['volume_ma_19w']  = talib.MA(df.volume, timeperiod=daily_count*5*19)
        # df['volume_ma_20w']  = talib.MA(df.volume, timeperiod=daily_count*5*20)
        
        
        # df['volume_sma_02w']  = talib.SMA(df.volume, timeperiod=daily_count*5*2)
        # df['volume_sma_03w']  = talib.SMA(df.volume, timeperiod=daily_count*5*3)
        # df['volume_sma_04w']  = talib.SMA(df.volume, timeperiod=daily_count*5*4)
        # df['volume_sma_05w']  = talib.SMA(df.volume, timeperiod=daily_count*5*5)
        # df['volume_sma_06w']  = talib.SMA(df.volume, timeperiod=daily_count*5*6)
        # df['volume_sma_07w']  = talib.SMA(df.volume, timeperiod=daily_count*5*7)
        # df['volume_sma_08w']  = talib.SMA(df.volume, timeperiod=daily_count*5*8)
        # df['volume_sma_09w']  = talib.SMA(df.volume, timeperiod=daily_count*5*9)
        # df['volume_sma_10w']  = talib.SMA(df.volume, timeperiod=daily_count*5*10)
        # df['volume_sma_11w']  = talib.SMA(df.volume, timeperiod=daily_count*5*11)
        # df['volume_sma_12w']  = talib.SMA(df.volume, timeperiod=daily_count*5*12)
        # df['volume_sma_13w']  = talib.SMA(df.volume, timeperiod=daily_count*5*13)
        # df['volume_sma_14w']  = talib.SMA(df.volume, timeperiod=daily_count*5*14)
        # df['volume_sma_15w']  = talib.SMA(df.volume, timeperiod=daily_count*5*15)
        # df['volume_sma_16w']  = talib.SMA(df.volume, timeperiod=daily_count*5*16)
        # df['volume_sma_17w']  = talib.SMA(df.volume, timeperiod=daily_count*5*17)
        # df['volume_sma_18w']  = talib.SMA(df.volume, timeperiod=daily_count*5*18)
        # df['volume_sma_19w']  = talib.SMA(df.volume, timeperiod=daily_count*5*19)
        # df['volume_sma_20w']  = talib.SMA(df.volume, timeperiod=daily_count*5*20)
        
        
        # df['volume_avg_02w'] = (df.volume_ema_02w + df.volume_ma_02w + df.volume_sma_02w)/3
        # df['volume_avg_03w'] = (df.volume_ema_03w + df.volume_ma_03w + df.volume_sma_03w)/3
        # df['volume_avg_04w'] = (df.volume_ema_04w + df.volume_ma_04w + df.volume_sma_04w)/3
        # df['volume_avg_05w'] = (df.volume_ema_05w + df.volume_ma_05w + df.volume_sma_05w)/3
        # df['volume_avg_06w'] = (df.volume_ema_06w + df.volume_ma_06w + df.volume_sma_06w)/3
        # df['volume_avg_07w'] = (df.volume_ema_07w + df.volume_ma_07w + df.volume_sma_07w)/3
        # df['volume_avg_08w'] = (df.volume_ema_08w + df.volume_ma_08w + df.volume_sma_08w)/3
        # df['volume_avg_09w'] = (df.volume_ema_09w + df.volume_ma_09w + df.volume_sma_09w)/3
        # df['volume_avg_10w'] = (df.volume_ema_10w + df.volume_ma_10w + df.volume_sma_10w)/3
        # df['volume_avg_11w'] = (df.volume_ema_11w + df.volume_ma_11w + df.volume_sma_11w)/3
        # df['volume_avg_12w'] = (df.volume_ema_12w + df.volume_ma_12w + df.volume_sma_12w)/3
        # df['volume_avg_13w'] = (df.volume_ema_13w + df.volume_ma_13w + df.volume_sma_13w)/3
        # df['volume_avg_14w'] = (df.volume_ema_14w + df.volume_ma_14w + df.volume_sma_14w)/3
        # df['volume_avg_15w'] = (df.volume_ema_15w + df.volume_ma_15w + df.volume_sma_15w)/3
        # df['volume_avg_16w'] = (df.volume_ema_16w + df.volume_ma_16w + df.volume_sma_16w)/3
        # df['volume_avg_17w'] = (df.volume_ema_17w + df.volume_ma_17w + df.volume_sma_17w)/3
        # df['volume_avg_18w'] = (df.volume_ema_18w + df.volume_ma_18w + df.volume_sma_18w)/3
        # df['volume_avg_19w'] = (df.volume_ema_19w + df.volume_ma_19w + df.volume_sma_19w)/3
        # df['volume_avg_20w'] = (df.volume_ema_20w + df.volume_ma_20w + df.volume_sma_20w)/3

        return df

# if __name__ == '__main__':
#     matches_df = pd.read_csv('matches.csv', dtype={'sto_id':str})
#     sto_ids_backup = matches_df.sto_id.tolist()
#     sto_ids_backup.sort()
#     delta = 30
#     daily_count = int(240 / delta)
#     bsa = BaosAgent(sto_ids_backup)
#     df = bsa.read_freq_df(30, sto_ids_backup[0])
#     df = FeatureTool.add_atr_ft(df, daily_count, 90)
#     print(df.iloc[-8:])

    