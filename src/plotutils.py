#coding=utf-8

import os
import numpy as np
import matplotlib.pyplot as plt

class PlotTool:

    subplot_height = 3

    @staticmethod
    def custom_ax(ax):
        ax.set_facecolor('#2A2A2A')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_color('gray')
        ax.spines['bottom'].set_color('gray')
        ax.spines['left'].set_color('gray')
        ax.tick_params(color='gray')
    
    @staticmethod
    def custom_axticks(ax, xaxis_idxes, x_axis_slice):
        plt.sca(ax)
        plt.xticks(xaxis_idxes[x_axis_slice], fontsize=8, rotation=10, color='w')
        plt.yticks(fontsize=8, color='w')

    @staticmethod
    def align_yaxis(ax1, ax2, base):
        ax1_ymin, ax1_ymax = ax1.get_ylim()
        ax2_ymin, ax2_ymax = ax2.get_ylim()
        new_ax2_ymax = (base-ax2_ymin) / ((base-ax1_ymin) / (ax1_ymax - ax1_ymin)) +  ax2_ymin
        new_ax1_ymax = (base-ax1_ymin) / ((base-ax2_ymin) / (ax2_ymax - ax2_ymin)) +  ax1_ymin
        if new_ax2_ymax >= ax2_ymax:
            ax2.set_ylim(ax2_ymin, new_ax2_ymax)
        else:
            ax1.set_ylim(ax1_ymin, new_ax1_ymax)

    @staticmethod
    def plot_figure(df, daily_count, obs_idxes, save_flag=False):
        subplot_num = 7
        subplot_idx = 0
        fig = plt.figure(figsize=(.25 * len(df)/daily_count, subplot_num * PlotTool.subplot_height))
        fig.patch.set_facecolor('#2A2A2A')
        
        # xaxis_idxes = df.time.values
        xaxis_idxes = df.time.str[:4] + '-' + df.time.str[4:6] + '-' + df.time.str[6:8] + ' ' + df.time.str[8:10] + ':' + df.time.str[10:12]
        # print(xaxis_idxes.iloc[-1])
        x_axis_slice = slice(0, -1, daily_count * 5)
        
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        ax.plot(xaxis_idxes, df.close,      lw=.5, color='orange')
        ax.plot(xaxis_idxes, df.closema_4w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_3w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_2w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_5d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_4d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_3d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_2d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_1d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_1h, lw=.1, color='orange')
        cond_macdhist1d_k1d_up = (df.macdhist_1d > df.macdhist_1d.shift(1)) & (df.k_1d > df.k_1d.shift(1))
        # min_y = min(df.close)
        # max_y = max(df.close)
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=(df.macdhist_1d >= df.macdhist_1d.shift(1)), facecolor='orangered',  alpha=0.1)
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=(df.k_1d >= df.k_1d.shift(1)), facecolor='lime',  alpha=0.1)
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        ax2.fill_between(xaxis_idxes, 0, df.volume, facecolor='cyan', alpha=.2)
        ax2.plot(xaxis_idxes, df.vol_ma_4w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_3w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_2w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_5d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_4d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_3d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_2d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_1d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_1h, lw=.1, color='cyan')
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)
        
        ####################################
        ### 量价相关性
        ####################################
        # subplot_idx += 1
        # ax = plt.subplot(subplot_num,1,subplot_idx)
        # PlotTool.custom_ax(ax)
        # # ax.plot(xaxis_idxes, df.close, lw=.5, color='orange')
        # ax.plot(xaxis_idxes, df.volume_slope, lw=.5, color='cyan')
        # ax.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.1)
        # cond_tgt = (df.closema_avg > df.closema_avg.shift(1)) & (df.closema_avg.shift(1) < df.closema_avg.shift(2))
        # PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        # ax2 = ax.twinx()
        # PlotTool.custom_ax(ax2)
        # ax2.plot(xaxis_idxes, df.close_slope, lw=.5, color='orange')
        # ax2.fill_between(xaxis_idxes, 0, df.corr_close_vol, facecolor='orangered', where=df.volume_slope > 0, alpha=.2)
        # ax2.fill_between(xaxis_idxes, 0, df.corr_close_vol, facecolor='lime', where=df.volume_slope < 0, alpha=.2)
        # for obs_idx in obs_idxes:
        #     ax2.vlines(xaxis_idxes[obs_idx], -1, 1, lw=.2, color='w')
        # # ### 量升价升
        # # ax2.fill_between(xaxis_idxes, 0, df.corr_closema_volma, where=(df.closema_avg > df.closema_avg.shift(1)) & (df.vol_log_ma_avg > df.vol_log_ma_avg.shift(1)), facecolor='royalblue',   alpha=.2)
        # # ### 量升价跌
        # # ax2.fill_between(xaxis_idxes, df.corr_closema_volma, 0, where=(df.closema_avg < df.closema_avg.shift(1)) & (df.vol_log_ma_avg > df.vol_log_ma_avg.shift(1)), facecolor='cyan',   alpha=.2)
        # # ### 量跌价升
        # # ax2.fill_between(xaxis_idxes, df.corr_closema_volma, 0, where=(df.closema_avg > df.closema_avg.shift(1)) & (df.vol_log_ma_avg < df.vol_log_ma_avg.shift(1)), facecolor='orange', alpha=.2)
        # # ### 量跌价跌
        # # ax2.fill_between(xaxis_idxes, 0, df.corr_closema_volma, where=(df.closema_avg < df.closema_avg.shift(1)) & (df.vol_log_ma_avg < df.vol_log_ma_avg.shift(1)), facecolor='orangered',    alpha=.2)
        # PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)
        # PlotTool.align_yaxis(ax, ax2, 0)

        ####################################
        ### 量价移动平均线
        ####################################
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        cond_closema_duotou = (df.closema_1h > df.closema_1d) & (df.closema_1d > df.closema_2d) & (df.closema_2d > df.closema_3d) & (df.closema_3d > df.closema_4d) & (df.closema_4d > df.closema_5d) & (df.closema_5d > df.closema_2w) & (df.closema_2w > df.closema_3w) & (df.closema_3w > df.closema_4w)
        cond_volma_duotou = (df.vol_log_ma_1h > df.vol_log_ma_1d) & (df.vol_log_ma_1d > df.vol_log_ma_2d) & (df.vol_log_ma_2d > df.vol_log_ma_3d) & (df.vol_log_ma_3d > df.vol_log_ma_4d) & (df.vol_log_ma_4d > df.vol_log_ma_5d)# & (df.vol_log_ma_5d > df.vol_log_ma_2w) & (df.vol_log_ma_2w > df.vol_log_ma_3w) & (df.vol_log_ma_3w > df.vol_log_ma_4w)
        cond_closema_increase = df.closema_avg > df.closema_avg.shift(1)
        cond_volma_increase = (df.vol_log_ma_avg > df.vol_log_ma_avg.shift(1))
        ax.plot(xaxis_idxes, df.closema_4w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_3w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_2w, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_5d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_4d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_3d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_2d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_1d, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_1h, lw=.1, color='orange')
        ax.plot(xaxis_idxes, df.closema_avg, lw=.5, color='orange')
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        # min_y = min(min(df.closema_4w), min(df.closema_3w), min(df.closema_2w), min(df.closema_5d), min(df.closema_4d), min(df.closema_3d), min(df.closema_2d), min(df.closema_1d), min(df.closema_1h))
        # max_y = max(max(df.closema_4w), max(df.closema_3w), max(df.closema_2w), max(df.closema_5d), max(df.closema_4d), max(df.closema_3d), max(df.closema_2d), max(df.closema_1d), max(df.closema_1h))
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=cond_closema_increase, facecolor='orange', alpha=0.1)
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        ax2.plot(xaxis_idxes, df.vol_ma_4w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_3w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_2w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_5d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_4d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_3d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_2d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_1d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_1h, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.vol_ma_avg, lw=.5, color='cyan')
        # min_y = min(min(df.vol_ma_4w), min(df.vol_ma_3w), min(df.vol_ma_2w), min(df.vol_ma_5d), min(df.vol_ma_4d), min(df.vol_ma_3d), min(df.vol_ma_2d), min(df.vol_ma_1d), min(df.vol_ma_1h))
        # max_y = max(max(df.vol_ma_4w), max(df.vol_ma_3w), max(df.vol_ma_2w), max(df.vol_ma_5d), max(df.vol_ma_4d), max(df.vol_ma_3d), max(df.vol_ma_2d), max(df.vol_ma_1d), max(df.vol_ma_1h))
        # ax2.fill_between(xaxis_idxes, min_y, max_y, where=cond_volma_duotou, facecolor='cyan', alpha=0.1)
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)

        ####################################
        ### macd_1t 斜率，macd_1t 与价格相关性
        ####################################
        # subplot_idx += 1
        # ax = plt.subplot(subplot_num,1,subplot_idx)
        # slopes = df.macdhist_1t.rolling(4).apply(compute_slopes, raw=True)
        # corrs  = df.macdhist_1t.rolling(4).corr(df.close)
        # PlotTool.custom_ax(ax)
        # ax.plot(xaxis_idxes, slopes, lw=.5, color='orange')
        # ax.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.3)
        # custom_axticks(ax, xaxis_idxes, x_axis_slice)
        # ax2 = ax.twinx()
        # PlotTool.custom_ax(ax2)
        # ax2.plot(xaxis_idxes, corrs,  lw=.5, color='cyan')
        # ax2.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.3)
        # ax2.vlines(xaxis_idxes[obs_idx], -1, 1, lw=.2, color='w')
        # custom_axticks(ax2, xaxis_idxes, x_axis_slice)
        # align_yaxis(ax, ax2, 0)


        ####################################
        ### MACD
        ####################################
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        ax.plot(xaxis_idxes, df.close, lw=.5, color='orange')
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        # min_y = np.min(df.close)
        # max_y = np.max(df.close)
        # cond_pailei = (df.macdhist_avg_w > df.macdhist_avg_w.shift(1))
        # cond_pailei = (df.macdhist_avg_d > df.macdhist_avg_d.shift(1)) & cond_pailei
        # cond_macd_dlong = (df.macdhist_1d > df.macdhist_1d.shift(1)) & (df.macdhist_2d > df.macdhist_2d.shift(1)) & (df.macdhist_3d > df.macdhist_3d.shift(1)) & (df.macdhist_4d > df.macdhist_4d.shift(1))
        # cond_macd_wlong = (df.macdhist_1w > df.macdhist_1w.shift(1)) & (df.macdhist_2w > df.macdhist_2w.shift(1)) & (df.macdhist_3w > df.macdhist_3w.shift(1)) & (df.macdhist_4w > df.macdhist_4w.shift(1))
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=cond_macd_dlong, facecolor='red',  alpha=0.3)
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=cond_macd_wlong, facecolor='lime',  alpha=0.3)
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=cond_pailei, facecolor='cyan',  alpha=0.2)
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        line_width=.1
        ax2.plot(xaxis_idxes, df.macdhist_4w,    lw=line_width, color='fuchsia')
        ax2.plot(xaxis_idxes, df.macdhist_3w,    lw=line_width, color='fuchsia')
        ax2.plot(xaxis_idxes, df.macdhist_2w,    lw=line_width, color='fuchsia')
        ax2.plot(xaxis_idxes, df.macdhist_1w,    lw=line_width, color='fuchsia')
        ax2.plot(xaxis_idxes, df.macdhist_avg_w, lw=.5, color='fuchsia')
        ax2.plot(xaxis_idxes, df.macdhist_4d,    lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_3d,    lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_2d,    lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_1d,    lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_avg_d, lw=.5, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_2h,    lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1h,    lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_hh,    lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t,    lw=.2, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_avg_h, lw=.5, color='cyan')
        ax2.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=1)
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)

        ####################################
        ### MACD Hist Sum
        ####################################
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        ax.plot(xaxis_idxes, df.close, lw=.5, color='orange')
        # max_y = np.max(df.close)
        # min_y = np.min(df.close)
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_0hh > df.macdhist_1t_sum_last_0hh.shift(1))
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_01h > df.macdhist_1t_sum_last_01h.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_02h > df.macdhist_1t_sum_last_02h.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_03h > df.macdhist_1t_sum_last_03h.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_01d > df.macdhist_1t_sum_last_01d.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_02d > df.macdhist_1t_sum_last_02d.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_03d > df.macdhist_1t_sum_last_03d.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_04d > df.macdhist_1t_sum_last_04d.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_01w > df.macdhist_1t_sum_last_01w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_04w > df.macdhist_1t_sum_last_04w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_08w > df.macdhist_1t_sum_last_08w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_12w > df.macdhist_1t_sum_last_12w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_16w > df.macdhist_1t_sum_last_16w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_20w > df.macdhist_1t_sum_last_20w.shift(1)) & cond_all_macdhist_up
        # cond_all_macdhist_up = (df.macdhist_1t_sum_last_24w > df.macdhist_1t_sum_last_24w.shift(1)) & cond_all_macdhist_up
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=cond_all_macdhist_up, facecolor='cyan',  alpha=0.3)
        # cond_vol_clp_up = (df.vol_log_ma_avg > df.vol_log_ma_avg.shift(1)) & (df.closema_avg > df.closema_avg.shift(1))
        # for cond_idx in df[cond_volma_duotou & cond_closema_duotou].index:
        #     ax.vlines(xaxis_idxes[cond_idx], np.min(df.close), np.max(df.close), lw=1, color='cyan')
        
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        line_width = .2
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_0hh, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_01h, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_02h, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_03h, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_01d, lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_02d, lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_03d, lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_04d, lw=line_width, color='yellow')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_01w, lw=line_width, color='yellow')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_02w, lw=line_width, color='orangered')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_03w, lw=line_width, color='orangered')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_04w, lw=line_width, color='fuchsia')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_05w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_06w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_07w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_08w, lw=line_width, color='fuchsia')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_09w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_10w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_11w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_12w, lw=line_width, color='fuchsia')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_13w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_14w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_15w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_16w, lw=line_width, color='fuchsia')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_17w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_18w, lw=line_width, color='cyan')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_19w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_20w, lw=line_width, color='fuchsia')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_21w, lw=line_width, color='magenta')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_22w, lw=line_width, color='magenta')
        # ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_23w, lw=line_width, color='magenta')
        ax2.plot(xaxis_idxes, df.macdhist_1t_sum_last_24w, lw=line_width, color='magenta')
        ax2.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.5)
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)

        ####################################
        ### K指标
        ####################################
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        ax.plot(xaxis_idxes, df.close, lw=.5, color='orange')
        # cond_sp = (df.k_1t < 35) & (df.k_1h > 70) & (df.k_1d > 35) & (df.k_1d < 50)
        # cond_sp = df.k_1d > 85
        # ax.fill_between(xaxis_idxes, min(df.close), max(df.close), where=cond_sp, facecolor='red',  alpha=0.2)
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        # min_y = np.min(df.close)
        # max_y = np.max(df.close)
        # ax.fill_between(xaxis_idxes, min_y, max_y, where=df.k_1d > df.k_1d.shift(1), facecolor='cyan',  alpha=0.3)
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        ax2.plot(xaxis_idxes, df.k_4w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_3w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_2w, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_5d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_4d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_3d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_2d, lw=.1, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1d, lw=.5, color='cyan')
        # ax2.plot(xaxis_idxes, df.k_1h, lw=.5, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t, lw=.5, color='cyan')
        ax2.hlines(20, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.1)
        ax2.hlines(50, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.2)
        ax2.hlines(80, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.1)
        ax2.fill_between(xaxis_idxes, df.k_1d, 50, where=df.k_1d < 50, facecolor='cyan', alpha=0.3)
        ax2.fill_between(xaxis_idxes, df.k_1d, 20, where=df.k_1d < 20, facecolor='cyan', alpha=0.3)
        ax2.fill_between(xaxis_idxes, 50, df.k_1d, where=df.k_1d > 50, facecolor='orange', alpha=0.3)
        ax2.fill_between(xaxis_idxes, 80, df.k_1d, where=df.k_1d > 80, facecolor='orange', alpha=0.3)
        # cond_ks = (df.k_2d > df.k_2d.shift(1)) & (df.k_3d > df.k_3d.shift(1)) & (df.k_4d > df.k_4d.shift(1)) & (df.k_5d > df.k_5d.shift(1)) & (df.k_5d > df.k_5d.shift(1)) & (df.k_2w > df.k_2w.shift(1)) & (df.k_3w > df.k_3w.shift(1)) & (df.k_4w > df.k_4w.shift(1))
        # cond_k_1t_min = (df.k_1t > df.k_1t.shift(1)) & (df.k_1t.shift(1) < df.k_1t.shift(2)) & (df.k_1t.shift(1) < 50)
        # for cond_idx in df[cond_ks & cond_k_1t_min].index:
        #     ax2.vlines(xaxis_idxes[cond_idx], np.min(df.k_1t), np.max(df.k_1t), lw=.5, color='orange')
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)

        ####################################
        ### K Sum
        ####################################
        subplot_idx += 1
        ax = plt.subplot(subplot_num,1,subplot_idx)
        PlotTool.custom_ax(ax)
        ax.plot(xaxis_idxes, df.close, lw=.5, color='orange')
        cond_ksum_all_up = (df.k_1t_sum_last_01d > df.k_1t_sum_last_01d.shift(1))
        cond_ksum_all_up = (df.k_1t_sum_last_02d > df.k_1t_sum_last_02d.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_03d > df.k_1t_sum_last_03d.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_04d > df.k_1t_sum_last_04d.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_01w > df.k_1t_sum_last_01w.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_02w > df.k_1t_sum_last_02w.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_03w > df.k_1t_sum_last_03w.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_04w > df.k_1t_sum_last_04w.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_08w > df.k_1t_sum_last_08w.shift(1)) & cond_ksum_all_up
        cond_ksum_all_up = (df.k_1t_sum_last_12w > df.k_1t_sum_last_12w.shift(1)) & cond_ksum_all_up
        cond_allksum = (df.k_1t_sum_last_01d\
                        + df.k_1t_sum_last_02d\
                        + df.k_1t_sum_last_03d\
                        + df.k_1t_sum_last_04d\
                        + df.k_1t_sum_last_01w\
                        + df.k_1t_sum_last_02w\
                        + df.k_1t_sum_last_03w\
                        + df.k_1t_sum_last_04w\
                        + df.k_1t_sum_last_08w\
                        + df.k_1t_sum_last_12w) > 0
        cond_k1d_up = df.k_1d > df.k_1d.shift(1)
        for cond_idx in df[cond_allksum & cond_k1d_up & cond_closema_duotou].index:
            ax.vlines(xaxis_idxes[cond_idx], np.min(df.close), np.max(df.close), lw=.5, color='orange')
        # for obs_idx in obs_idxes:
        #     ax.vlines(xaxis_idxes[obs_idx], np.min(df.close), np.max(df.close), lw=.2, color='w')
        PlotTool.custom_axticks(ax, xaxis_idxes, x_axis_slice)
        ax2 = ax.twinx()
        PlotTool.custom_ax(ax2)
        line_width = .2
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_01d, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_02d, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_03d, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_04d, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_01w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_02w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_03w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_04w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_08w, lw=line_width, color='cyan')
        ax2.plot(xaxis_idxes, df.k_1t_sum_last_12w, lw=line_width, color='cyan')
        ax2.hlines(0, xmin=min(xaxis_idxes), xmax=max(xaxis_idxes), color='w', lw=.5)
        PlotTool.custom_axticks(ax2, xaxis_idxes, x_axis_slice)

        if save_flag:
            stoid = df.iloc[-1].code
            date = df.iloc[-1].date
            ts = df.iloc[obs_idxes[-1]].time[4:]
            
            fig_path = './target/' + date[-5:] + '-' + ts[-4:] + '/'
            if not os.path.exists(fig_path):
                os.mkdir(fig_path)
            full_fn = fig_path + stoid + '.png'

            plt.savefig(full_fn, bbox_inches='tight', dpi=512, transparent=True)
            print('save figure to ' + full_fn)

        plt.show()
        plt.close('all')