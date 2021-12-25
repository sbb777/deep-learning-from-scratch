import numpy as np

X = np.array([1,2])
W1 = np.array([[1,2,3],[4,5,6]])
A1 = np.dot(X,W1)

print(A1)

B1 = np.array([1,2,3])

A11 = A1 + B1
print(A11)