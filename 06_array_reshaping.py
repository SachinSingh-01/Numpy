import numpy as np
arr=np.arange(12)
print("Original array",arr)
reshaped=arr.reshape((3,4))
print("\n Reshaped array",reshaped)
flattend=reshaped.flatten()
print("\n Flattend array",flattend)

raveled=reshaped.ravel()
print("\n raveled array",raveled)

transpose=reshaped.T
print("\n  Transposed array",transpose)
