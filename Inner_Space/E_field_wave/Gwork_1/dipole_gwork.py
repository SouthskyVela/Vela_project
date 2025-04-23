import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']  #enable CHINESE
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

k=8.987551*pow(10,9)
q_1=(1.6)*pow(10,-19)
q_2=(-1.6)*pow(10,-19)
r_deta=0.1

fig=plt.figure()  #返回一个figure对象
ax=fig.add_subplot(111,projection='3d') 
#在fig对象中添加一个子图(第一行第一个第一列,"3d"三维坐标系)
#给ax返回一个子图对象

x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)
X,Y=np.meshgrid(x,y)


#设置标题与坐标轴
ax.set_title('用来测试的画布',fontsize=20)
ax.set_xlabel('x',fontsize=16)
ax.set_ylabel('y',fontsize=16)
ax.set_zlabel('z',fontsize=16)

plt.show()