import numpy as np
import matplotlib.pyplot as plt

# 创建一维坐标数组
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

# 生成二维网格
X, Y = np.meshgrid(x, y)
print(X)

# # 打印结果
# print("X:\n", X)
# print("Y:\n", Y)

# # 可视化
# plt.figure(figsize=(8, 6))
# plt.contour(X, Y, np.sin(np.sqrt(X**2 + Y**2)), levels=20)
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Contour plot of sin(sqrt(X^2 + Y^2))')
# plt.show()
