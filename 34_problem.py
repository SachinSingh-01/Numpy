'''Create a random 5x4 array.
Normalize each column'''
import numpy as np
random_array=np.random.randint(1,20,(5,4))
print(random_array)
mean=np.mean(random_array,axis=0)
std=np.std(random_array,axis=0)
normalize=(random_array-mean)/std
print("\nMean:",mean)
print("\nSTD:",std)
print("\nNormalize:",normalize)