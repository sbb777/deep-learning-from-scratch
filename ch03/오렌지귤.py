import numpy as np
import random

x_data = []
for i in range(100):
    x_data.append([random.randint(7,20), random.randint(80,130)])
    x_data.append([random.randint(1,10), random.randint(50,100)])
y_data = []
for i in range(100):
    y_data.append(1)
    y_data.append(0)

X_train = np.array(x_data)
# print(X_train)
print(X_train.shape)
print(X_train.ndim)

X_train = X_train.reshape(200,2)
# print(X_train)
print(X_train.shape)

'''
(200, 2)
(200, 2)
reshape 을 안해도 원래 (200, 2) 였음. 강사 에러
'''
