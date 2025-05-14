import numpy as np
import matplotlib.pyplot as plt

# 定义时间轴
def generate_time_axis(duration, fs):
    return np.arange(0, duration + 1/fs, 1/fs)

# 定义单位阶跃函数
def unit_step(t):
    return np.where(t > 0, 1, 0)

# 定义信号f(t)
def f_t(t, num_terms=100):
    result = np.zeros_like(t)
    for n in range(num_terms):
        result += unit_step(t - n) - unit_step(t - n - 0.1)
    return result

# 定义信号s(t)
def s_t(t):
    f_t_val = f_t(t)
    return f_t_val * np.cos(400 * np.pi * t)

# 采样信号
def sample_signal(t, fs):
    return s_t(t)

# 绘制信号
def plot_signals(t, original_signal, fs1, fs2):
    plt.figure(figsize=(12, 8))

    # 确保时间轴在0到0.125秒内
    t_mask = t <= 0.125

    # 原始信号
    plt.subplot(3, 1, 1)
    plt.plot(t[t_mask], original_signal[t_mask])
    plt.title('Original Signal s(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # 采样信号1
    t_sampled1 = generate_time_axis(0.125, fs1)
    s_sampled1 = sample_signal(t_sampled1, fs1)
    plt.subplot(3, 1, 2)
    plt.stem(t_sampled1, s_sampled1, linefmt='r', markerfmt='ro', basefmt=" ", label=f'Sampled at {fs1} Hz')
    plt.title(f'Sampled Signal at {fs1} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # 采样信号2
    t_sampled2 = generate_time_axis(0.125, fs2)
    s_sampled2 = sample_signal(t_sampled2, fs2)
    plt.subplot(3, 1, 3)
    plt.stem(t_sampled2, s_sampled2, linefmt='b', markerfmt='bo', basefmt=" ", label=f'Sampled at {fs2} Hz')
    plt.title(f'Sampled Signal at {fs2} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# 参数设置
duration = 0.125 # 信号持续时间调整到0.125秒
fs1 = 1000 # 采样率1
fs2 = 500 # 采样率2

# 生成时间轴
t = generate_time_axis(duration, 10000) # 原始信号的采样率为10000 Hz

# 计算原始信号
original_signal = s_t(t)

# 绘制信号
plot_signals(t, original_signal, fs1, fs2)
