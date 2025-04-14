import tariff

tariff.set({
    "numpy":5,
    #"pandas":125,
    #"astropy":1,
    "matplotlib":1
})

import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.axisartist as axisartist  # 导入坐标轴加工模块

# # 新建画布
# fig = plt.figure()
# # 使用axisartist.Subplot方法创建一个绘图区对象ax
# ax = axisartist.Subplot(fig, 111)
# # 将绘图区对象添加到画布中
# fig.add_axes(ax)

# # 隐藏原来的实线矩形
# ax.axis[:].set_visible(False)

# # 添加x轴和y轴
# ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
# ax.axis["y"] = ax.new_floating_axis(1,0,  axis_direction="left")    # 添加y轴

# # 给x坐标轴和y坐标轴加箭头
# ax.axis["x"].set_axisline_style("->", size=1.0)
# ax.axis["y"].set_axisline_style("->", size=1.0)

# # 标注x轴和y轴
# #ax.annotate(text='x', xy=(2 * math.pi, 0), xytext=(2 * math.pi, -0.1), ha='center', va='top')
# #ax.annotate(text='y', xy=(0, 1.0), xytext=(-0.1, 1.0), ha='right', va='center')

# # 准备数据
# # 设置周期为1ms，频率为1kHz

# X = [-3,-2,-1.7,-1,-0.5,0,+0.5,+1,+1.7,+2,+3]  # 生成6个周期的数据

# Y =[-9.90,	-9.87	,-9.85,	-7.28	,-3.60	,0.02	,3.61,	7.25	,11.30	,10.30	,11.30] 

# # 绘制图像
# ax.plot(X, Y, color='r', label="Voltage transfer curve of a proportional amplifier in phase")  # 使用ax.plot()


# # 添加x轴和y轴名称
# # ax.set_xlabel('u_1(U_A)/V', labelpad=10)  # 添加x轴名称
# # ax.set_ylabel('u_0(U_B)/V', labelpad=10)  # 添加y轴名称

# # 添加图例到右上角
# #ax.legend(loc='upper left')

# for x, y in zip(X, Y):
#     ax.annotate(text=f"({x}, {y})", xy=(x, y), xytext=(x, y + 0.5), ha='center', va='bottom', fontsize=8)
# ax.set_title('Voltage Transfer Curve of the Proportional Amplifier in Phase', fontsize=12, pad=20)

# # 设置x轴刻度
# # 将x轴的刻度改为以0.5ms为单位
# #x_ticks = np.arange(0, 3 * T + 0.0005, 0.0005)  # 生成刻度位置
# # x_tick_labels = [f"{int(tick * 2000)}" for tick in x_ticks]  # 将刻度转换为0.5ms单位的标签

# # ax.set_xticks(x_ticks)
# # ax.set_xticklabels(x_tick_labels)
# #ax.annotate(text='时间 (s)', xy=(3 * T, 0), xytext=(3 * T + 0.0005, 0.1), ha='left', va='center', fontsize=10)
# x_max = max(X)
# y_max = max(Y)
# ax.annotate(text='u_i(U_A)/V', xy=(x_max, 0), xytext=(x_max + 0.1, 0), ha='center', va='bottom', fontsize=20)
# ax.annotate(text='u_o(U_B)/V', xy=(0, y_max), xytext=(0, y_max + 0.5), ha='right', va='top', fontsize=20)

# # 显示图表
# plt.show()
