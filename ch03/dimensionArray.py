import numpy as np

A=np.array([[1],[2],[3],[4]])
print(A)
nd=np.ndim(A)
print(nd)

print(A.shape)

print(A.shape[0])
print(A.shape[1])
# print(A.shape[2])
print('####'*30)

A=np.array([1,2,3,4])
print(A)
nd=np.ndim(A)
print(nd)

print(A.shape)

print(A.shape[0])
print(A.shape[1])
# print(A.shape[2])
print('####'*30)

A=np.array([[1,[2]],[2],[3],[4]]) # 에러
print(A)
nd=np.ndim(A)
print(nd)

print(A.shape)

print(A.shape[0])
print(A.shape[1])
# print(A.shape[2])