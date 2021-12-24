import matplotlib.pylab as plt
import numpy as np


x=np.arange(-5,5,0.1)
y=np.sin(x)
y1=y*y

plt.plot(x,y,'rs',x,y1,'b--')
plt.ylim(-1.1, 1.1)
plt.show()
