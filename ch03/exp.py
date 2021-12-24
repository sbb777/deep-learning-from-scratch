import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5.1, 5.1, 0.1)
y=np.exp(x)
y1=np.exp(-x) # = y2=1/np.exp(x)
y2=1/np.exp(x)

plt.plot(x,y,x,y1,'r--',x,y2,'gs')
plt.show()