import matplotlib.pyplot as plt
import scipy as sp


t = sp.arange(-2, 2, 0.2)
X,Y = sp.meshgrid(t, t)
Z = X * sp.exp( -X**2-Y**2 )
DX,DY = sp.gradient(Z, 0.2)

plt.contour(X, Y, Z)
plt.quiver(X, Y, DX, DY)
plt.show()
