'''Create a 2D array and print:
Shape
Number of dimensions
Total number of elements'''
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print("2d array",arr_2d)

print("Shape:",arr_2d.shape)
print("Dimension:",arr_2d.ndim)
print("Total no. of element:",arr_2d.size)