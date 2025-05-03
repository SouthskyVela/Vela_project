import numpy as np
import matplotlib.pyplot as plt

# 设置字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 启用中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 常量
k = 8.987551e9  # 库仑常数
q = 1.6e-19  # 电荷量
l = 1e-10  # 电偶极子长度
p = q * l  # 电偶极矩

# 创建网格点
x = np.linspace(-1e-8, 1e-8, 100)
y = np.linspace(-1e-8, 1e-8, 100)
x, y = np.meshgrid(x, y)

# 计算每个点的电势
r = np.sqrt(x**2 + y**2)  # 到原点的距离
theta = np.arctan2(y, x)  # 极角

# 电偶极子的电势公式
U = k * p * np.cos(theta) / r**2

# 绘制等势线
plt.figure(figsize=(8, 8))
contour = plt.contour(x, y, U, levels=10000, cmap='viridis')  # 绘制10000条等势线
plt.colorbar(contour, label='电势 U (V)')  # 添加颜色条

# 设置标题和坐标轴标签
plt.title('电偶极子在 z=0 平面上的等势线', fontsize=20)
plt.xlabel('x (m)', fontsize=16)
plt.ylabel('y (m)', fontsize=16)

# 显示图形
plt.show()
