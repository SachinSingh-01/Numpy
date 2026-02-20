'''Create an array from 1 to 12 and reshape it into:
3 rows and 4 columns'''
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Without reshape:",arr)

reshaped=arr.reshape(3,4)
print(reshaped)