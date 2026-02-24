'''Replace Values Based on Condition
arr = np.array([5,12,7,18,3,25])
Replace:
All values greater than 10 with -1'''
import numpy as np
arr = np.array([5,12,7,18,3,25])
arr[arr>10]=-1
print(arr)
