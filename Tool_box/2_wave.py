import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.axisartist as axisartist  # 导入坐标轴加工模块

# 新建画布
fig = plt.figure()
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)

# 隐藏原来的实线矩形
ax.axis[:].set_visible(False)

# 添加x轴和y轴
ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="left")    # 添加y轴

# 给x坐标轴和y坐标轴加箭头
ax.axis["x"].set_axisline_style("->", size=1.0)
ax.axis["y"].set_axisline_style("->", size=1.0)

# 标注x轴和y轴
ax.annotate(text='x', xy=(2 * math.pi, 0), xytext=(2 * math.pi, -0.1), ha='center', va='top')
ax.annotate(text='y', xy=(0, 1.0), xytext=(-0.1, 1.0), ha='right', va='center')

# 准备数据
# 设置周期为1ms，频率为1kHz
T = 0.001  # 周期为1ms
f = 1000   # 频率为1kHz
X = np.linspace(0, 3 * T, 1000, endpoint=True)  # 生成6个周期的数据
C = np.sin(2 * np.pi * f * X)  # 余弦波
S = -5*np.sin(2 * np.pi * f * X)  # 正弦波

# 绘制图像
ax.plot(X, C, color='b', label="U(input) Function")  # 使用ax.plot()
ax.plot(X, S, color='r', label="U(output) Function")  # 使用ax.plot()

# 添加x轴和y轴名称
ax.set_xlabel('ms', labelpad=10)  # 添加x轴名称
ax.set_ylabel('Custom unit voltage', labelpad=10)  # 添加y轴名称

# 添加图例到右上角
ax.legend(loc='upper right')

# 设置x轴刻度
# 将x轴的刻度改为以0.5ms为单位
x_ticks = np.arange(0, 3 * T + 0.0005, 0.0005)  # 生成刻度位置
x_tick_labels = [f"{int(tick * 2000)}" for tick in x_ticks]  # 将刻度转换为0.5ms单位的标签

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels)
#ax.annotate(text='时间 (s)', xy=(3 * T, 0), xytext=(3 * T + 0.0005, 0.1), ha='left', va='center', fontsize=10)

# 显示图表
plt.show()
