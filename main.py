# Write a Python program to find the sum of all elements in a multi-dimensional array.
multiarray=[[1,2,3],[4,5,6],[7,8,9]]
total_sum=0
for i in range(len(multiarray)):
    for j in range(len(multiarray[i])):
        total_sum+=multiarray[i][j]
print(total_sum)

#with numpy module
import numpy as np
multiarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
total_sum=np.sum(multiarray)
print(total_sum)

import numpy as np
# Define the multi-dimensional array
multiarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
total_product = np.prod(multiarray)
print(total_product)

import numpy as np
arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])
print(np.dot(arr1,arr2.T))

import numpy as np
arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])
print(np.cross(arr1,arr2))
