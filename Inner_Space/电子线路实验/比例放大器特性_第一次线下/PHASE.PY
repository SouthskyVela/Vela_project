import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.optimize import fsolve
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

# 给定的x和y数据
x_data = [0.1, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 250, 300, 350, 450]
y_data = [5.200, 5.360, 5.360, 5.000, 5.000, 5.066, 5.000, 4.812, 4.750, 4.765, 4.647, 4.556, 4.440, 4.315, 4.264, 4.095, 3.952, 3.81, 3.636, 3.000, 2.441, 2.167, 1.744]

# 将数据转换为numpy数组
x = np.array(x_data)
y = np.array(y_data)

# 扩展曲线至y=0
# 定义一个函数，用于求解y=0时的x值
def find_x_for_y_zero(x):
    return spline(x)

# 使用make_interp_spline生成平滑曲线
x_smooth = np.linspace(min(x), max(x), 500)  # 创建平滑的x轴数据
spline = make_interp_spline(x, y, k=3)  # 创建三次样条插值
y_smooth = spline(x_smooth)  # 根据插值生成平滑的y轴数据

# 绘制平滑曲线
plt.plot(x_smooth, y_smooth, color='red', label='幅频特性曲线')

# 标注每个数据点
plt.scatter(x, y, color='blue', s=50, zorder=5)  # 使用蓝色实心圆点标注

# 显示原点(0,0)
plt.scatter(0, 0, color='black', s=20, zorder=5)

# 在Au等于3.7895处找到对应的x值
target_y = 3.7895
# 使用插值找到对应的x值
target_x = x_smooth[np.argmin(np.abs(y_smooth - target_y))]

# 在该点处用蓝色三角形标注
plt.scatter(target_x, target_y, color='green', marker='^', s=25, zorder=5)

# 画虚线垂线
plt.axvline(x=target_x, color='blue', linestyle='--', linewidth=1, zorder=4)
plt.axhline(y=target_y, color='blue', linestyle='--', linewidth=1, zorder=4)

# 设置坐标轴标签
plt.xlabel('f(_input)/kHz')
plt.ylabel('Au')

# 在虚线垂线与y轴交汇处标注0.707|Au|
plt.text(0, target_y, f'0.707|Au|', fontsize=10, color='blue', verticalalignment='bottom', horizontalalignment='left')

# 在虚线垂线与x轴交汇处标注f_H
plt.text(target_x, 0, f'f_H', fontsize=10, color='blue', verticalalignment='top', horizontalalignment='left')

# 使用fsolve求解y=0时的x值
x_zero = fsolve(find_x_for_y_zero, max(x_smooth))[0]  # 初始猜测值为x的最大值

# 绘制延长线至y=0
x_extended = np.linspace(min(x_smooth), x_zero, 500)
y_extended = spline(x_extended)
plt.plot(x_extended, y_extended, color='red', linestyle='--', label='Extended Curve')

# 标注y=0处的x值
plt.scatter(x_zero, 0, color='green', s=100, zorder=5)
plt.text(x_zero, 0, f'x={x_zero:.2f}', fontsize=10, color='green', verticalalignment='top', horizontalalignment='right')

# 在y=3.7895处的点旁边标注x,y坐标值
plt.text(target_x, target_y, f'({target_x:.2f}, {target_y:.2f})', fontsize=10, color='blue', verticalalignment='bottom', horizontalalignment='left')

# 在x=0处找到对应的y值
x_zero_point = 0
y_zero_point = spline(x_zero_point)

# 在该点处用绿色点标记
plt.scatter(x_zero_point, y_zero_point, color='green', s=25, zorder=5)

# 在该点旁边标注y轴的值
plt.text(x_zero_point, y_zero_point, f'y={y_zero_point:.2f}', fontsize=10, color='green', verticalalignment='bottom', horizontalalignment='left')


# 显示图例
plt.legend()

# 显示图形
plt.show()



