empty_list = list()
also_empty_list = []
zeros_list = [0] * 5
print zeros_list

list_var = range(10)
print list_var

import numpy as np

M = np.array([[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]])
v = np.array([[1],
 [2],
 [3]])
 
 print(M.shape)
 
 print(v.shape)
 
 print(v + v)
 
v_single_dim = np.array([1, 2, 3])
print(v_single_dim.shape)

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
M = np.vstack([v1, v2, v3])
print(M)

print(M[:2, 1:3])

print(M.dot(v))

print v.T.dot(v)
