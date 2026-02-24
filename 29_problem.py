'''Create two matrices:
A (2x3)
B (3x2)
Perform:
Matrix multiplication
Element-wise multiplication
Explain difference between both.'''
import numpy as np
arr_1=np.random.randint(1,10,(2,3))
arr_2=np.random.randint(1,10,(3,2))
print("Array one",arr_1)
print("Array Two",arr_2)
mul=arr_1 @ arr_2
print("Multiplcation:",mul)

transverse=arr_1 * arr_2.T
print("Element wise multiplication:",transverse)