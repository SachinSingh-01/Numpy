'''Create a 3x3 array and find
Sum of each row
Sum of each column'''
import numpy as np
arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print("Array:")
print(arr)

row_sums = arr.sum(axis=1)
print("Sum of each row:", row_sums)

col_sums = arr.sum(axis=0)
print("Sum of each column:", col_sums)
