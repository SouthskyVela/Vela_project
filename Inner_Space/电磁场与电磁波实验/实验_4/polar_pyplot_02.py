import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# 创建一个新的图形窗口
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 数据
angles_degrees = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])  # 角度数据
power_readings = np.array([-48.6, -49.4, -52.5, -54.2, -54.3, -55.3, -51.6, -50, -45.5, -46.1, -44.2, -44.5, -44.7])  # 功率读数（dBm）

# 应用高斯平滑
sigma = 1  # 高斯平滑的标准差，可以根据需要调整
power_readings_smoothed = gaussian_filter1d(power_readings, sigma)

# 将角度转换为弧度
angles_radians = np.deg2rad(angles_degrees)

# 绘制径向网格线
ax.set_rgrids([0, 30, 60, 90], angle=0, labels=[0, 30, 60, 90])  # 设置径向网格线

# 绘制角度网格线，包括0°到360°的所有角度
full_circle_angles = np.arange(0, 361, 15)
ax.set_thetagrids(full_circle_angles, labels=[f'{int(angle)}°' for angle in full_circle_angles])

# 绘制上半平面的数据
ax.plot(angles_radians, power_readings_smoothed, color='blue', linewidth=2)

# 对称映射到下半平面
angles_radians_lower = np.deg2rad(360 - angles_degrees)
ax.plot(angles_radians_lower, power_readings_smoothed, color='blue', linewidth=2)

# 绘制同心圆
theta = np.linspace(0, 2 * np.pi, 360, endpoint=False)
rho = np.linspace(-55.3, -44.2, 5)
for r in rho:
    ax.plot(theta, r * np.ones_like(theta), color='black', alpha=0.25, linestyle='-')

# 添加图例
ax.legend()

# 显示图形
plt.show()
