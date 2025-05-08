import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题
# 定义距离和电位数据
distance = np.linspace(0, 9, 10)  # 距离从0到9
voltage_data = np.array([
    [9.75, 9.71, 9.65, 9.6, 9.54, 9.52, 9.52],
    [9.04, 9.02, 8.82, 7.92, 8.67, 8.82, 8.75],
    [8.23, 8.15, 8.06, 8.03, 7.97, 7.98, 7.99],
    [7.37, 7.3, 7.38, 7.27, 7.29, 7.15, 7.26],
    [6.46, 6.64, 6.5, 6.46, 6.41, 6.41, 6.42],
    [5.87, 5.8, 5.8, 5.61, 5.48, 5.55, 5.51],
    [4.87, 4.98, 4.9, 4.84, 4.83, 4.9, 4.88],
    [4.12, 4.15, 4.23, 4.11, 4.1, 4.08, 3.51],
    [3.41, 3.4, 3.38, 3.38, 3.31, 3.37, 3.33],
    [2.62, 2.64, 2.63, 2.63, 2.48, 2.55, 2.73]
])  #取每组数据的第三到第八列取平均数来在上述代码中生成10个数据点，然后绘图

# 计算每组数据的第三到第八列的平均值
voltage_experimental = np.mean(voltage_data, axis=1)

# 定义理想电位分布曲线
voltage_theoretical = 12 - (12/10) * distance

# 创建图形和轴
fig, ax1 = plt.subplots()

# 绘制实验曲线和理论曲线
ax1.plot(distance, voltage_experimental, 'go-', label='实验曲线', color='green')  # 绿色曲线，带红点
ax1.plot(distance, voltage_theoretical, label='理论曲线', color='orange')  # 橘色曲线

# 在曲线上用点标记出数据点
ax1.scatter(distance, voltage_experimental, color='red')

# 设置轴标签和标题
ax1.set_xlabel('距离')
ax1.set_ylabel('电位（10组数据平均值）', color='green')
ax1.set_title('平行板电容器电位距离曲线图')

# 添加图例
ax1.legend(loc='upper right')

# 创建第二个y轴，共享x轴
ax2 = ax1.twinx()
ax2.plot(distance, voltage_theoretical, label='理想电位分布', color='orange')
ax2.set_ylabel('电位（理论值）', color='orange')

# 添加图例
ax2.legend(loc='upper right')

# 显示图形
plt.show()
