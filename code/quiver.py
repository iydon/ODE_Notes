import numpy as np
import matplotlib.pyplot as plt


def direction_field_2d(x, y, xlim=None, ylim=None, num=None):
	xlim = xlim or [-10, 10]
	ylim = ylim or [-10, 10]
	num  = num or [10, 10]
	x_ = np.linspace(*xlim, num[0])
	y_ = np.linspace(*ylim, num[-1])
	X,Y = np.meshgrid(x_, y_)
	Zx = x(X, Y)
	Zy = y(X, Y)
	plt.quiver(X, Y, Zx, Zy)
	plt.show()

def direction_field_3d(x, y, z, xlim=None, ylim=None, zlim=None, num=None):
	xlim = xlim or [-10, 10]
	ylim = ylim or [-10, 10]
	zlim = zlim or [-10, 10]
	num  = num or [10, 10, 10]
	x_ = np.linspace(*xlim, num[0])
	y_ = np.linspace(*ylim, num[1])
	z_ = np.linspace(*zlim, num[2])
	X,Y,Z = np.meshgrid(x_, y_, z_)
	Zx = x(X, Y, Z)
	Zy = y(X, Y, Z)
	Zz = z(X, Y, Z)
	ax = plt.gca(projection="3d")
	ax.quiver3D(X, Y, Z, Zx, Zy, Zz)
	plt.show()


x = lambda x,y,z=None: y
y = lambda x,y,z=None: -np.sin(x) + 0.01*y
z = lambda x,y,z=None: np.cos(z)
xlim = [-2*np.pi, 2*np.pi]
ylim = [-2*np.pi, 2*np.pi]
zlim = [-2*np.pi, 2*np.pi]
direction_field_2d(x, y, xlim, ylim)
direction_field_3d(x, y, z, xlim, ylim, zlim, num=[5,5,5])
