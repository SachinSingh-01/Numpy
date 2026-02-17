import numpy as np
py_list=[1,2,3]
print("Python List multiplication",py_list*2)
import time
start=time.time()
py_list=[i*2 for i in range (100000000)]
print("\n List operation time:",time.time()-start)
start=time.time()
np_array=np.arange(100000000)*2
print("\n Numpy operation time:",time.time()-start)