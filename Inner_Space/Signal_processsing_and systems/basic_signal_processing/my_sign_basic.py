import wave_box
squ_n1=wave_box.square_wave(1.0,1.0)
squ_n1.squ_plt(start_time=-5.0,total_time=10.0,num=100,endpoint=True)
tooth_n1=wave_box.sawtooth_wave(2.0,2.5)
tooth_n1.toooth_plt(start_time=-5.0,total_time=10.0,num=50,endpoint=True)
#记得把相位设置加上！！
