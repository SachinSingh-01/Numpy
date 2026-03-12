                            #LEVEL-1

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


'''3.Create an array of 5 zeros.
Check its dtype.
Now create the same array but force dtype to int32.
What difference do you observe'''
# import numpy as np
# zero_float=np.zeros(5)
# print(zero_float)
# print("Type:",zero_float.dtype)
# zero_int=np.zeros(5,dtype='int')
# print(zero_int)
# print("Type:",zero_int.dtype)

'''4.Create an array using np.ones((2,3)).
What is its:
ndim,shape,size'''
# import numpy as np
# array_one=np.ones((2,3))
# print(array_one)
# # print("Dimension:",array_one.ndim)
# print("Shape:",array_one.shape)
# print("Size:",array_one.size)

                        # LEVEL-2
'''5.Create a 3D array with shape (2,3,4) using zeros.
Without printing the array, answer:
What is its ndim?
What is its size?
# How many elements are there in axis 1?'''
# import numpy as np
# array_3d=np.zeros((2,3,4))
# print(array_3d)
# # 2, 24
# print(array_3d.ndim)
# print(array_3d.shape)

'''6.Create an array using:
np.arange(3, 15, 3)
What is the output?
What is its dtype?
What is its shape?'''
# import numpy as np
# arange_array=np.arange(3,15,3)  #In numpy when you use single parenthesis to create zero,one etc array it through an error but in case of single 1d array u can use single parenthesis and in double size array u need to use double parenthesis and in case of arange u can use single parenthesis because it store info start stop step'''
# print(arange_array)
# print("Type:",arange_array.dtype)
# print("Shape:",arange_array.shape)

'''7.Create two arrays:
a = np.arange(0, 1, 0.2)
b = np.linspace(0, 1, 5)
Are they exactly same?
Why or why not?'''
# import numpy as np
# a = np.arange(0, 1, 0.2)
# b = np.linspace(0, 1, 5)
# print(a)
# print(b)

'''8.Create a 2D array of shape (4,4).
Now reshape it to (2,8).
Answer:
Why is this allowed?
What condition must always be true for reshape?'''
# import numpy as np
# array_2d=np.arange(16).reshape(4,4)
# print(array_2d)

# reshape_array=array_2d.reshape(2,8)
# print("Reshape to (2,8):",reshape_array)

                        # LEVEL-3

'''9.Create:
a = np.arange(10)
b = a[2:6]
Now change:
b[0] = 100
What happens to a?
Explain WHY this happens.'''
# import numpy as np
# a = np.arange(10)
# b = a[2:6].copy() 
# b[0] = 100
# print("Array a:", a)
# print("Array b:", b)

'''10.Create:
a = np.ones((3,3), dtype=np.int32)
Total memory used in bytes.
(Hint: int32 = 4 bytes)'''
# import numpy as np
# a=np.ones((3,3), dtype=np.int32)
# print(a.nbytes)

'''11.If an array has:
shape = (5,4,3)
dtype = float64
Answer:
ndim
size
total memory usage in bytes'''
# import numpy as np
# a=np.zeros((5,4,3),dtype=np.float64)
# print("Ndim:",a.ndim)
# print("Shape:",a.size)
# print("Total memory use:",a.nbytes)

'''12.You are storing grayscale images:
100 images
Each image size 28x28
dtype = float32
Answer:
What should be the shape?
What is ndim?
What is total memory used (in bytes)?'''
# import numpy as np
# a=np.zeros((100,28,28), dtype=np.float32)
# print("Ndim:",a.ndim)
# print("Shape:",a.shape)
# print("Total memory use:",a.nbytes)

'''13.Create a NumPy array containing numbers from 1 to 10.
Print:shape,size,ndim'''
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print("Shape:",arr.shape)
# print("Size:",arr.size)
# print("Ndim:",arr.ndim)

'''14.Create an array of 5 zeros and another array of 5 ones.
Add them together and print the result.
Expected logic: element-wise addition.'''
# import numpy as np
# arr_zeros=np.zeros(5)
# arr_ones=np.ones(5)
# print(arr_zeros)
# print(arr_ones)
# print("Sum of array:",arr_zeros+arr_ones)

'''15.Create this array:
[10, 20, 30, 40, 50]
Print:first element,last element,middle element.'''
# import numpy as np
# arr=np.array([10, 20, 30, 40, 50])
# print("First element:",arr[0])
# print("Last element:",arr[-1])
# print("Middle element:",arr[2])

'''16.Create this array:
[1,2,3,4,5,6,7,8,9,10]
Slice the array to get:
[4,5,6,7]'''
# import numpy as np
# arr_1d=np.array([1,2,3,4,5,6,7,8,9,10])
# print("Slice:",arr_1d[3:7])

'''17.Create a 2x3 array of ones.
Print its:shape,size,ndim'''
# import numpy as np
# arr_ones=np.ones((2,3))
# print(arr_ones)
# print("Shape:",arr_ones.shape)
# print("Size:",arr_ones.size)
# print("Ndim:",arr_ones.ndim)

'''18. Create an array using:
np.arange(1,21)
Select only the numbers greater than 10.'''
# import numpy as np
# arr=np.arange(1,21)
# print("Number greater than 10:",arr[arr>10])

'''19.Create this array:
[1,2,3,4,5,6,7,8,9,10]
Select only the even numbers'''
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print("Even number:",arr[arr%2==0])

'''20.Create a 3x4 array using np.arange() and reshape().
Example structure:
[[1 2 3 4]
 [5 6 7 8]
 [9 10 11 12]]
Find:sum of all elements,sum of rows,sum of columns'''
# import numpy as np
# arr=np.arange(1,13).reshape((3,4))
# print(arr)
# print("Sum of all the element:",arr.sum())
# print("Sum across rows:",arr.sum(axis=1))
# print("Sum across columns:",arr.sum(axis=0))

'''21.Create a 1D array
[1,2,3,4,5,6]
Convert it into:a row vector,a column vector'''
# import numpy as np
# arr_1d=np.array([1,2,3,4,5,6])
# print("Row vector:",arr_1d.reshape(1,-1))
# print("Column vector:",arr_1d.reshape(-1,1))

'''22.Create this array:
[5,10,15,20,25]
Multiply every element by 3 using broadcasting.'''
# import numpy as np
# arr_mul=np.array([5,10,15,20,25])
# print("Multiply by 3:",arr_mul*3)

'''23.Create two arrays:
a1 =
[[1,1],
 [2,2]]
a2 =
[[3,3],
 [4,4]]
Stack them:vertically,horizontally'''
# import numpy as np
# a1 =np.array([[1,1],
#             [2,2]])
# a2 =np.array([[3,3],
#             [4,4]])
# print("Vertically stack:",np.vstack((a1,a2)))
# print("Horizontally stack:",np.hstack((a1,a2)))

'''24.Create this array:
np.arange(1,25).reshape(2,12)
Split it into 3 equal arrays using hsplit().'''
# import numpy as np
# arr=np.arange(1,25).reshape(2,12)
# print(arr)
# print("Split:",np.hsplit(arr,3))

'''25.Using the same array, split it after column 4 and column 8.'''
# import numpy as np
# arr = np.arange(1, 25).reshape(2, 12)
# parts = np.split(arr, [4, 8], axis=1)
# for i, p in enumerate(parts):
#     print(f"Part {i+1}:\n{p}\n")

'''26.Create this array:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Extract the second row and modify its first value.'''
# import numpy as np
# arr=np.array([[1,2,3],
#  [4,5,6],
#  [7,8,9]])
# second_row=arr[1]

# second_row[0]=99
# print(arr)

'''27.Now repeat the previous question but use .copy() before modifying.
Check if the original array changes.'''
# import numpy as np
# arr=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# second_row=arr[1].copy()

# second_row[0]=45
# print("Original array:",arr)
# print(second_row)

'''28.Create a 3x3 matrix:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Add this vector using broadcasting:'''
# import numpy as np
# arr=np.array([[1,2,3],
# [4,5,6],
# [7,8,9]])
# vector=np.array([10,20,30])
# result=arr+vector
# print(result)

'''29.Create a 4x4 random integer matrix.
Select all numbers that are:
greater than 5
less than 12'''
# import numpy as np

# random_arr=np.random.randint(1,20,(4,4))
# print(random_arr)
# print("Number greater than 5:",random_arr[random_arr>5])
# print("Number less than 12:",random_arr[random_arr<12])

'''30.Create this array:
[3,7,1,9,5]
Sort the array.
Then print the index positions of sorted elements using argsort().'''
# import numpy as np
# arr=np.array([3,7,1,9,5])
# print("Sorted:",arr.sort())
# print("Index sort:",arr.argsort())

'''31.Create an array from 1 to 12.
Reshape it into 3x4, then reshape it again into 2x6.
Explain why this works.'''
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Reshape to 3x4:",arr.reshape(3,4))
# print("Reshape to 2x6:",arr.reshape(2,6))

'''32.You are storing 100 grayscale images.
Each image size = 28x28
dtype = float32
What should be the array shape?
What is ndim?
How many elements are stored?
Total memory used in bytes?'''
# import numpy as np
# arr=np.zeros((28,28,100))
# print("Ndim:",arr.ndim)
# print("Shape:",arr.shape)
# print("Total memory use:",arr.nbytes)

'''33.Create two arrays:
a1 =
[[1,1],
 [2,2]]
a2 =
[[3,3],
 [4,4]]
Stack them:
vertically
horizontally'''
# import numpy as np
# a1 =[[1,1],
#  [2,2]]
# a2 =[[3,3],
#  [4,4]]
# vertically_stack=np.vstack((a1,a2))
# horizontally_stack=np.hstack((a1,a2))
# print("Vertically:",vertically_stack)
# print("Horizontally:",horizontally_stack)

'''34.Create this array:
np.arange(1,25).reshape(2,12)
Split it into 3 equal arrays.'''
# import numpy as np
# arr=np.arange(1,25).reshape(2,12)
# split=np.array_split(arr,3)
# print(split)
# print(arr)
# print("\nSplit arrays:")
# for i, sub_array in enumerate(split):
#     print(f"Part {i+1}:")
#     print(sub_array)

'''35.Create a 3x3 matrix.
Select:
first row
last column'''
import numpy as np
arr=np.random.randint(1,12,(3,3))
print(arr)
element=arr[0,-1]
print(element)