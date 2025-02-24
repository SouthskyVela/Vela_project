import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#import code.thinkdsp as thinkdsp

class square_wave:
    def __init__(self,frquency,amplitude):
        self.freq=frquency
        self.amp=amplitude
    def squ_plt(self,start_time,total_time,num,endpoint):
        x_label=np.linspace(start_time,start_time+total_time,num,endpoint)
        y_label=self.amp * signal.square(2*np.pi*self.freq*x_label)
        plt.plot(x_label,y_label)
        plt.xlabel('Time')
        plt.ylabel("Amplitude")
        plt.title('square wave')
        plt.grid(True) #添加网格
        plt.show()