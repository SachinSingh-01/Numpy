'''1.Create a 1D array containing numbers from 1 to 5.
Print ndim,shape,size,dtype'''
# import numpy as np
# array=np.array([1,2,3,4,5])
# print("Dimension:",np.ndim(array))
# print("Shape:",np.shape(array))
# print("Size:",np.size(array))
# print("Dtype:",array.dtype)

'''2.Create a 2D array:
[[10, 20, 30],
 [40, 50, 60]]
Print:ndim,shape,size'''
# import numpy as np
# arr_2d=([[10, 20, 30],
#         [40, 50, 60]])
# print("Dimension:",np.ndim(arr_2d))
# print("Shape:",np.shape(arr_2d))
# print("Size:",np.size(arr_2d))


'''Create an array of 5 zeros.
Check its dtype.
Now create the same array but force dtype to int32.
What difference do you observe'''
import numpy as np
zero_float=np.zeros(5)
print(zero_float)
print("Type:",zero_float.dtype)
zero_int=np.zeros(5,dtype='int')
print(zero_int)
print("Type:",zero_int.dtype)