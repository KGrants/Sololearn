import numpy as np

x = np.arange(0,100,3)
y = np.arange(0,100,5)
z = np.intersect1d(x,y)

print(z[z>0])