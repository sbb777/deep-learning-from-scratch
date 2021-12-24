import numpy as np

def step_function(x):
    y=x>0
    return y.astype(np.int)
    # return y

'''
a=step_function(5)
print(a)

AttributeError: 'bool' object has no attribute 'astype'
에러발생
'''

x=np.array([-1.0, 1.0, 2.0])
print(x)

a=step_function(x)
print(a)