                            #LEVEL-1

'''1.Create a 1D array containing numbers from 1 to 5.
Print ndim,shape,size,dtype'''
import numpy as np
array=np.array([1,2,3,4,5])
print("Dimension:",np.ndim(array))
print("Shape:",np.shape(array))
print("Size:",np.size(array))
print("Dtype:",array.dtype)

'''2.Create a 2D array:
[[10, 20, 30],
 [40, 50, 60]]
Print:ndim,shape,size'''
import numpy as np
arr_2d=([[10, 20, 30],
        [40, 50, 60]])
print("Dimension:",np.ndim(arr_2d))
print("Shape:",np.shape(arr_2d))
print("Size:",np.size(arr_2d))


'''3.Create an array of 5 zeros.
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

'''4.Create an array using np.ones((2,3)).
What is its:
ndim,shape,size'''
import numpy as np
array_one=np.ones((2,3))
print(array_one)
# print("Dimension:",array_one.ndim)
print("Shape:",array_one.shape)
print("Size:",array_one.size)

                        # LEVEL-2
'''5.Create a 3D array with shape (2,3,4) using zeros.
Without printing the array, answer:
What is its ndim?
What is its size?
How many elements are there in axis 1?'''
import numpy as np
array_3d=np.zeros((2,3,4))
print(array_3d)
# 2, 24
print(array_3d.ndim)
print(array_3d.shape)

'''6.Create an array using:
np.arange(3, 15, 3)
What is the output?
What is its dtype?
What is its shape?'''
import numpy as np
arange_array=np.arange(3,15,3)  #In numpy when you use single parenthesis to create zero,one etc array it through an error but in case of single 1d array u can use single parenthesis and in double size array u need to use double parenthesis and in case of arange u can use single parenthesis because it store info start stop step'''
print(arange_array)
print("Type:",arange_array.dtype)
print("Shape:",arange_array.shape)

'''7.Create two arrays:
a = np.arange(0, 1, 0.2)
b = np.linspace(0, 1, 5)
Are they exactly same?
Why or why not?'''
import numpy as np
a = np.arange(0, 1, 0.2)
b = np.linspace(0, 1, 5)
print(a)
print(b)

'''8.Create a 2D array of shape (4,4).
Now reshape it to (2,8).
Answer:
Why is this allowed?
What condition must always be true for reshape?'''
import numpy as np
array_2d=np.arange(16).reshape(4,4)
print(array_2d)

reshape_array=array_2d.reshape(2,8)
print("Reshape to (2,8):",reshape_array)

                        # LEVEL-3