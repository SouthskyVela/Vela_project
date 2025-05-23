import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']  #enable CHINESE
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

k=8.987551*pow(10,9)
q1=(1.6)*pow(10,-19)
q2=(-1.6)*pow(10,-19)
q3=(1.6)*pow(10,-19)
q1_s=[1,0,3]
q2_s=[2,1,0]
q3_s=[0,1,1]

fig=plt.figure()  #返回一个figure对象
ax=fig.add_subplot(111,projection='3d') 
#在fig对象中添加一个子图(第一行第一个第一列,"3d"三维坐标系)
#给ax返回一个子图对象

# x=np.linspace(-10,10,1000)
# y=np.linspace(-10,10,1000)
# X,Y=np.meshgrid(x,y)
# z_p=pow(x**2+y**2,0.5)

a = 3  # 长轴
b = 2  # 短轴

# 参数方程绘制椭圆
theta = np.linspace(0, 2 * np.pi, 100)  # 参数角度
x = a * np.cos(theta)  # 椭圆的 x 坐标
y = b * np.sin(theta)  # 椭圆的 y 坐标
z = np.zeros_like(theta)  # z = 0
for i in range(-25,25,0.5):
    ax.plot(x,y,i,label='Ellipse', color='b')
# 绘制椭圆
#ax.plot(x, y, z, label='Ellipse', color='b')

#设置标题与坐标轴
ax.set_title('用来测试的画布',fontsize=20)
ax.set_xlabel('x',fontsize=16)
ax.set_ylabel('y',fontsize=16)
ax.set_zlabel('z',fontsize=16)

plt.show()