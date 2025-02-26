import math
import signal
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import code.thinkdsp as thinkdsp
#激活venv终端代码:.\.venv\Scripts\activate
#取消激活则是:      deactivate

cos_sig=thinkdsp.CosSignal(freq=2200,amp=1.0,offset=0)
sin_sig=thinkdsp.SinSignal(4400,2,0)
CosSin_mix=cos_sig+sin_sig   
#由于__add__的存在,两个被实例化的变量可以直接相加
sc_mixwwave=CosSin_mix.make_wave(0.5,-0.25,11)
#用新造出来的变量通过make_wave函数返回一个Signal对象
sc_mixwwave.plot()
plt.show()

# # create a square wave
# squ_frequency=1.0 #Hz
# period=1.0/squ_frequency
# squ_amplitude=1.0 #振幅
# squ_start_time=-5.0
# squ_Total_time=10.0 

# squ_t=np.linspace(squ_start_time,squ_start_time+squ_Total_time,num=100,endpoint=True)
# squ_sign_value=squ_amplitude*signal.square(2*np.pi*squ_frequency*squ_t)
# plt.plot(squ_t,squ_sign_value)
# #squ_wave_creation=np.where()
# plt.xlabel('TIME')
# plt.ylabel('Amplitude')
# plt.title('Square Wave')
# plt.grid(True)  #添加网格
# plt.show()