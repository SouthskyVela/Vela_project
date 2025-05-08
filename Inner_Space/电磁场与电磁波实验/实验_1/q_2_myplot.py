import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 原始数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
z = np.array([
    [6.18, 7.17, 7.66, 8.04, 8.13, 8.06, 7.73, 7.34, 6.78, 5.70],
    [4.57, 5.65, 6.09, 6.56, 6.64, 6.68, 6.29, 5.94, 5.30, 4.25],
    [3.67, 4.55, 4.99, 5.23, 5.30, 5.23, 4.87, 4.42, 3.84, 3.08],
    [2.75, 3.31, 3.66, 3.80, 3.85, 3.75, 3.38, 2.98, 2.51, 2.00],
    [2.02, 2.35, 2.56, 2.65, 2.67, 2.56, 2.29, 1.97, 1.65, 1.32],
    [1.50, 1.67, 1.79, 1.85, 1.86, 1.76, 1.56, 1.34, 1.12, 0.91],
    [1.14, 1.22, 1.31, 1.35, 1.36, 1.28, 1.14, 0.99, 0.84, 0.70],
    [0.87, 0.92, 0.97, 0.99, 0.99, 0.93, 0.83, 0.72, 0.61, 0.51],
    [0.67, 0.70, 0.74, 0.75, 0.74, 0.68, 0.60, 0.52, 0.44, 0.37],
    [0.57, 0.58, 0.59, 0.60, 0.59, 0.55, 0.49, 0.43, 0.37, 0.32]
])

# 确保z是一维数组
z = z.flatten()

# 创建网格点
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# 将x和y转换为网格点坐标
xgrid, ygrid = np.meshgrid(x, y)
points = np.vstack((xgrid.flatten(), ygrid.flatten())).T

# 拟合数据
zi = griddata(points, z, (xi, yi), method='linear')

# 计算电场分量
dx = xi[1, 0] - xi[0, 0]
dy = yi[0, 1] - yi[0, 0]

Ex, Ey = np.gradient(-zi, dx, dy)

# 找到最接近X=3、Y=7的点
index_x = np.searchsorted(xi[0, :], 3)
index_y = np.searchsorted(yi[:, 0], 7)

# 计算电场强度
E_x = Ex[index_y, index_x]
E_y = Ey[index_y, index_x]
E = np.sqrt(E_x**2 + E_y**2)

# 绘制曲面图并标记点
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xi, yi, zi, cmap='viridis', alpha=0.7)
ax.scatter(3, 7, zi[index_y, index_x], color='red', s=10)  # 标记红点
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Surface Plot of Potential Distribution')
plt.show()

x_points = np.array([2, 4, 3, 3])
y_points = np.array([7, 7, 6, 8])

# 重新构造 z 为二维数组
z_2d = z.reshape((10, 10))
index_points = [(np.searchsorted(x, x_point), np.searchsorted(y, y_point)) for x_point, y_point in zip(x_points, y_points)]
# 重新获取这些点上的电势值
z_points = np.array([z_2d[y_index, x_index] for x_index, y_index in index_points])

# 重新计算电场分量
# 电场 x 分量: (V(4, 7) - V(2, 7)) / (4 - 2)
E_x_manual = (z_points[1] - z_points[0]) / (4 - 2)

# 电场 y 分量: (V(3, 8) - V(3, 6)) / (8 - 6)
E_y_manual = (z_points[3] - z_points[2]) / (8 - 6)

# 电场强度
E_manual = np.sqrt(E_x_manual**2 + E_y_manual**2)

E_manual, E_x_manual, E_y_manual  # 返回电场强度的总大小和分量
print(E_manual,E_x_manual,E_y_manual)

