'''Given:
[10, 25, 30, 45, 50]
Print only numbers greater than 30.'''
import numpy as np
arr=np.array([10,25,30,45,50])
filtered_arr= arr[arr>30]
print("Number greater than 30:",filtered_arr)