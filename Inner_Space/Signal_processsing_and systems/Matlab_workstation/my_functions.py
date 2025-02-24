# save as my_functions.py
import numpy as np

def generate_random_array(size):
    """生成给定大小的随机数组，并返回其均值"""
    random_array = np.random.rand(size)
    mean_value = np.mean(random_array)
    return random_array.tolist(), mean_value

def helloworld():
    print(2306061)
