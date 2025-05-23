import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.patches import Circle
import return_E

nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

nq = 17  #在单位圆上添加nq个点电荷
charges = []
for i in range(nq):
    if i % 2 == 0:
        q = 1
    else:
        q = -1
    charges.append((q, (np.cos(2 * np.pi * i / nq), np.sin(2 * np.pi * i / nq))))
print (charges)

Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = return_E.E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey
fig = plt.figure()
ax = fig.add_subplot(111)
#添加画布对象

#使用streamplot函数绘制二维电场线(tnnd为什么不能适配3维绘图?????!)
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

# 可视化点电荷对象
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.show()