#返回网格在目标电荷下的场强结果
import numpy as np
def E(q, r0, x, y):
    den = np.hypot(x - r0[0], y - r0[1]) ** 3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den