# import numpy as np
# from scipy.optimize import minimize

# # 定义常量
# k = 1  # 库仑常数，假设为1

# # 定义电荷的位置和电荷量
# charges = [
#     (1, np.array([1, 0, 1])),
#     (-1, np.array([-1, 0, 1])),
#     (2, np.array([2, 1, 0]))
# ]

# # 定义电势方程的平方
# def potential_squared(z, x, y):
#     V = 0
#     for q, r in charges:
#         r1 = np.sqrt((x - r[0])**2 + (y - r[1])**2 + (z - r[2])**2)
#         V += k * q / r1
#     return (V - 2)**2

# # 定义 x 和 y 的值
# x = np.linspace(-10, 10, 50)
# y = np.linspace(-10, 10, 50)

# # 创建网格
# X, Y = np.meshgrid(x, y)

# # 初始化 z 的值
# Z = np.zeros_like(X)

# # 对每个 (x, y) 对进行迭代
# for i in range(X.shape[0]):
#     for j in range(X.shape[1]):
#         # 使用 minimize 求解 z，初始猜测值为 1
#         result = minimize(potential_squared, 1, args=(X[i, j], Y[i, j]))
#         Z[i, j] = result.x[0]

# # 打印结果
# print(Z)

import numpy as np
from scipy.optimize import minimize

# 定义常量
k = 1  # 库仑常数，假设为1

# 定义电荷的位置和电荷量
charges = [
    (1, np.array([1, 0, 1])),
    (-1, np.array([-1, 0, 1])),
    (2, np.array([2, 1, 0]))
]

# 定义电势方程的平方
def potential_squared(z, x, y):
    V = 0
    for q, r in charges:
        r1 = np.sqrt((x - r[0])**2 + (y - r[1])**2 + (z - r[2])**2)
        V += k * q / r1
    return (V - 2)**2

# 定义 x 和 y 的值
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

# 创建网格
X, Y = np.meshgrid(x, y)

# 初始化 z 的值
Z = np.zeros_like(X)

# 对每个 (x, y) 对进行迭代
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # 使用 minimize 求解 z，初始猜测值为 1
        result = minimize(potential_squared, 1, args=(X[i, j], Y[i, j]))
        Z[i, j] = result.x[0]

# 打印结果
print(Z)
