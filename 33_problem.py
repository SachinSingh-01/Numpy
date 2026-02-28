'''Create a random dataset:
100 rows
3 columns (3 features)
Compute:
Covariance matrix using NumPy'''
import numpy as np
random_number=np.random.randint(1,10,(100,3))
cov_matrix = np.cov(random_number, rowvar=False)
print(cov_matrix)
# print(random_number)