'''Find Duplicate Elements
Given:
arr = np.array([1,2,3,4,2,5,6,1,7])
All duplicate values
Unique values'''
import numpy as np
arr = np.array([1,2,3,4,2,5,6,1,7])
unique_value,count=np.unique(arr, return_counts=True)
duplicate_value=unique_value[count>1]
print("Unique values:",unique_value)
print("Duplicate values:",duplicate_value)