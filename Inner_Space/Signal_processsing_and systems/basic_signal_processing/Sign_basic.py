import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import code.thinkdsp as thinkdsp

cos_sig=thinkdsp.CosSignal(freq=440,amp=1.0,offset=0)
# create a square wave
squ_frequency=1.0 #Hz
period=1.0/squ_frequency
squ_amplitude=1.0 #振幅
squ_start_time=-5.0
squ_Total_time=10.0 

squ_t=np.linspace(squ_start_time,squ_start_time+squ_Total_time,num=100,endpoint=True)
squ_sign_value=squ_amplitude*signal.square(2*np.pi*squ_frequency*squ_t)
plt.plot(squ_t,squ_sign_value)
#squ_wave_creation=np.where()
plt.xlabel('TIME')
plt.ylabel('Amplitude')
plt.title('Square Wave')
plt.grid(True)  #添加网格
plt.show()