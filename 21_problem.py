'''Random Numbers
5 random numbers between 0 and 1
5 random integers between 1 and 50'''
import numpy as np
import random 
random1=np.random.rand(5)
random2=np.random.randint(1,50,5)
print(random1)
print(random2)