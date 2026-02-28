'''Create a 6x4 dataset of random numbers.
Manually insert some np.nan values.
Tasks:
Compute column-wise mean ignoring NaN.
Replace NaN values with the column mean.
Standardize the dataset'''
import numpy as np
array=np.random.randint(1,20,(6,4)).astype(float)
array[1,3]=np.nan
array[4,0]=np.nan
print("Dataset with NaN:",array)

mean=(np.nanmax(array,axis=0))
print("Column Mean (ignoring NaN):\n", mean)

inds = np.where(np.isnan(array))
array[inds] = np.take(mean, inds[1])
print("After Replacing NaN:\n", array)

std = np.std(array, axis=0)
X_std = (array - mean) / std
print("Standardized Data:\n", X_std)