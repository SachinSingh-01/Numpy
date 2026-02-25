'''Given:
arr = np.array([[1,50],
                [2,30],
                [3,40]])
Sort the array based on the second column.
Expected output:
Sorted by values 30, 40, 50.'''
import numpy as np
arr = np.array([[1,50],
                [2,30],
                [3,40]])

column_sort=arr[:,1].argsort() # here : this means take all row and 1 this means take the columns at index 1
sorted=arr[column_sort]
print(sorted)
# print(column_sort)