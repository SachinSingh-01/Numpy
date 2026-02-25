'''Create a 3x3 matrix.
Flatten it using .flatten()
Flatten using .ravel()
Now modify the raveled array and observe what happens to original array.
Explain why.'''
import numpy as np
arr=np.random.randint(1,10,(3,3))
print(arr)
f=arr.flatten()
print(f)
r=arr.ravel()
print(r)