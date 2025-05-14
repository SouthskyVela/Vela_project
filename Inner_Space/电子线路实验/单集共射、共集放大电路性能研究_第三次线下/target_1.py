import numpy as np
import matplotlib.pyplot as plt

# 设置时间范围
t = np.linspace(0, 1, 1000)  # 从0到1秒，1000个点

# 生成正弦波形
y = np.sin(2 * np.pi * 5 * t)  # 频率为5Hz的正弦波

# 添加截止失真
y_clipped = np.clip(y, -0.5, 1)  # 将波形限制在-1到1之间



# 绘制截止失真波形图
plt.subplot(2, 1, 2)
plt.plot(t, y_clipped, color='blue')  # 使用黄色线条
plt.title('Clipped Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
