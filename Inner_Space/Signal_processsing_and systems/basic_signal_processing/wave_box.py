import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#import code.thinkdsp as thinkdsp

class square_wave:
    def __init__(self,frquency,amplitude):
        self.freq=frquency
        self.amp=amplitude

        self.wave_shape_num=None
        self.wave_time=None
    def squ_plt(self,start_time,total_time,num,endpoint):
        x_label=np.linspace(start_time,start_time+total_time,num,endpoint)
        y_label=self.amp * signal.square(2*np.pi*self.freq*x_label)
        plt.plot(x_label,y_label)
        plt.xlabel('Time')
        plt.ylabel("Amplitude")
        plt.title('square wave')
        plt.grid(True) #添加网格
        plt.show()

        self.wave_shape_num=y_label
        self.wave_time=x_label

class  sawtooth_wave:
    def __init__(self,frquency,amplitude):
        self.freq=frquency
        self.amp=amplitude
        self.wave_shape_num=None
        self.wave_time=None
    def toooth_plt(self,start_time,total_time,num,endpoint):
        x_label=np.linspace(start_time,start_time+total_time,num,endpoint)
        y_label=self.amp * signal.sawtooth(2*np.pi*self.freq*x_label,width=0.25)
        plt.plot(x_label,y_label)
        plt.xlabel('Time')
        plt.ylabel("Amplitude")
        plt.title('sawtooth wave')
        plt.grid(True) #添加网格
        plt.show()

        self.wave_shape_num=y_label
        self.wave_time=x_label

#def wave_add(time,*all_wave):
    
