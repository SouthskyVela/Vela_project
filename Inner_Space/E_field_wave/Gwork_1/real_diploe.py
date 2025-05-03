import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']  #enable CHINESE
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

k=8.987551*pow(10,9)
q1=(1.6)*pow(10,-19)
q2=(-1.6)*pow(10,-19)
#q3=(1.6)*pow(10,-19)
q1_s=[0,1,0]
q2_s=[0,-1,0]
#q3_s=[0,1,1]

fig=plt.figure()  #返回一个figure对象
ax=fig.add_subplot(111,projection='3d') 
#在fig对象中添加一个子图(第一行第一个第一列,"3d"三维坐标系)
#给ax返回一个子图对象
theta=np.linspace(0,2*np.pi,100)
x=np.linspace(0,2*np.pi,100)
u=1
for z in range(-10,10):
    y=pow((k*q1*2*np.cos(theta)/u)-x**2-z**2,0.5)
    ax.plot(x,y,z,label='Ellipse', color='b')
#设置标题与坐标轴
ax.set_title('用来测试的画布',fontsize=20)
ax.set_xlabel('x',fontsize=16)
ax.set_ylabel('y',fontsize=16)
ax.set_zlabel('z',fontsize=16)

plt.show()