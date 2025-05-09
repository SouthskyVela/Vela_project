import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义参数
Pt = -29.10  # 发射功率（dBm），以20cm处的功率为基准
Gt = 1  # 发射天线增益（假设为单位增益，dBi）
Gr = 1  # 接收天线增益（假设为单位增益，dBi）
f = 1950e6  # 频率（Hz）

# 计算波长（米）
lambda_ = 3e8 / f

# 自由空间传播常数
k = 4 * np.pi / lambda_

# 创建距离数组（米）
distances = np.arange(0.2, 0.71, 0.05)  # 从20cm到70cm，步进5cm

# 初始化功率数组
powers = []

# 使用弗里斯传输方程计算功率
for distance in distances:
    Pr = Pt + Gt + Gr - 20 * np.log10(distance) - 20 * np.log10(f) + 147.55
    powers.append(Pr)

# 特定的距离点（米）
specific_distances = np.array([0.55, 0.60, 0.65, 0.70])

# 计算这些特定点的功率
specific_powers = Pt + Gt + Gr - 20 * np.log10(specific_distances) - 20 * np.log10(f) + 147.55

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(distances * 100, powers, marker='o', linestyle='-', label='功率曲线')
plt.scatter(specific_distances * 100, specific_powers, color='red')  # 标记特定点

# 添加特定点的功率标签
for i, txt in enumerate(specific_powers):
    plt.annotate(f'{specific_powers[i]:.2f} dBm', (specific_distances[i] * 100, specific_powers[i]), textcoords="offset points", xytext=(0,10), ha='center')

# 设置图表标题和轴标签
plt.xlabel('接收天线与发射天线之间的距离 (cm)')
plt.ylabel('功率 (dBm)')
plt.title('理想情况下电磁波在自由空间中的传输功率曲线')
plt.grid(True)
plt.legend()
plt.show()
