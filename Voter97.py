import matplotlib.pyplot as plt
import numpy as np
from math import pi as pi

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

d1=0
d2=1
X = np.arange(0, 3, 0.001)
Y = np.arange(-1, 1, 0.001)
X, Y = np.meshgrid(X, Y)
Z = np.cos(2*pi*X)*(1+d1*Y) + d2*pi*Y**2


surf = ax.plot_surface(X, Y, Z, cmap='hot',
                       linewidth=0, antialiased=False)
ax.set_xlabel(r'$q_{1}$')
ax.set_ylabel(r'$q_{2}$')
ax.set_zlabel(r'$V(q_{1},q_{2})$')


ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.axes.zaxis.set_ticklabels([])

ax.xaxis.labelpad=-10
ax.yaxis.labelpad=-10
ax.zaxis.labelpad=-10

plt.show()
plt.savefig("Voter97HD.png",dpi=600)
