import matplotlib.pyplot as plt
import numpy as np

def stepFunction(x):
    return np.array(x>0, dtype=np.int)

x=np.arange(-5.1, 5.1, 0.1)

rs=stepFunction(x)
print(rs)

plt.plot(x,rs)
plt.show()