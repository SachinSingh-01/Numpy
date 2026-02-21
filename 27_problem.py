'''Create a 4x4 random integer matrix.
Find:
Row sums
Index of row with maximum sum'''
import numpy as np
random_arr=np.random.randint(0,101,(4,4))
print(random_arr)

row_sum=random_arr.sum(axis=1)
print("Sum of first row:",row_sum)

max_index_sum=np.argmax(row_sum)
print("Maximum sum in first row:",max_index_sum)