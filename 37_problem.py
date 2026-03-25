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
# print("Shape:",a.shape)
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

'''28.Create a 3x3 random_arr:
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

'''29.Create a 4x4 random integer random_arr.
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
# print("Sorted:",np.sort(arr))
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

'''35.Create a 3x3 random_arr.
Select:
first row
last column'''
# import numpy as np
# arr=np.random.randint(1,12,(3,3))
# print(arr)
# print(arr[0])      # first row
# print(arr[:, -1])

'''36.Create a random_arr:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Find:
max value
min value
sum of elements'''
# import numpy as np
# arr=np.array([[1,2,3],
#  [4,5,6],
#  [7,8,9]])
# print("Maximum number:",arr.max())
# print("Minimum number:",arr.min())
# print("Sum of element:",arr.sum())

'''37.Find the sum of columns of the random_arr above'''
# import numpy as np
# arr=np.array([[1,2,3],
# [4,5,6],
# [7,8,9]])
# print("Sum of column:",arr.sum(axis=0))
# print("Sum of row:",arr.sum(axis=1))

'''38.Create this array:
[11,11,12,13,14,12,11]
Find unique values.'''
# import numpy as np
# arr=np.array([11,11,12,13,14,12,11])
# unique_number=np.unique(arr)
# print("Unique values:",unique_number)

'''39.Find count of each unique value.'''
# import numpy as np
# arr=np.array([11,11,12,13,14,12,11])
# count_unique=np.unique_counts(arr)
# print("Unique count=",count_unique)

'''40.Find indices of first occurrence of each unique value.'''
# import numpy as np
# arr=np.array([11,11,12,13,14,12,11])
# unique_number,first_occurrence=np.unique(arr,return_counts=True)
# print("Unique_number:",unique_number)
# print("Indices of first occurrence:",first_occurrence)

'''41.Create this random_arr:
[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [1,2,3,4]]
Find unique rows.'''
# import numpy as np
# arr=np.array([[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [1,2,3,4]])
# unique_rows=np.unique(arr,axis=0)
# print("Unique row:",unique_rows)

'''42.Create an array:
[3,7,1,9,5]
Sort the array.'''
# import numpy as np
# arr=np.array([3,7,1,9,5])
# sorted=np.sort(arr)
# print("Sorted array:",sorted)

'''43.Find the index positions of sorted elements using argsort().'''
# import numpy as np
# arr=np.array([3,7,1,9,5])
# index=np.argsort(arr)
# print(index)

'''44.Create a 5x5 random random_arr.
Find:
max of each column
min of each row'''
# import numpy as np
# arr=np.random.randint(2,22,(5,5))
# print(arr)
# Maximum_column=np.max(arr,axis=0)
# Minimum_row=np.min(arr,axis=1)
# print("Maximum columns:",Maximum_column)
# print("Minimum rows:",Minimum_row)

'''45.Create a dataset of 100 random integers between 0 and 50.
Find:mean,max,min,standard deviation'''
# import numpy as np
# arr=np.random.randint(1,100,size=100)
# print(arr)
# print("Maximum number:",arr.max())
# print("Minimum number:",arr.min())
# print("Minimum number:",arr.mean())
# print("Standard deviation:",arr.std())

'''46.Reshape that dataset into 10x10 random_arr.'''
# import numpy as np
# arr=np.random.randint(1,100,size=100)
# reshaping=np.reshape(arr,(10,10))
# print("Reshaping array:",reshaping)

'''47.Find unique values and their frequency.'''
# import numpy as np
# arr=np.random.randint(1,100,size=100)
# unique_number,count=np.unique(arr,return_counts=True)
# print("Unique number:",unique_number)
# print("Count=",count)

'''48.Normalize the random_arr by dividing all elements by 10.'''
# import numpy as np
# arr=np.random.randint(1,100,size=100)
# normalize=arr/10.0
# divideby10=(arr%10==0)
# divisible_element=arr[divideby10]
# print("Normalize array:",normalize)
# print("Number divisible by 10:",divisible_element)

'''49.Create a 4x4 random_arr.
Replace all values greater than 10 with 0.'''
# import numpy as np
# random_array=np.random.randint(1,20,(4,4))
# print("Array:",random_array)
# result=np.where(random_array>10,0,random_array)
# print("Number greater than 10:",result)

'''50.Find positions of values greater than 15 using np.nonzero().'''
# import numpy as np
# random_array=np.random.randint(1,20,(4,4))
# greater=np.nonzero(random_array>15)
# print("Number greater than 15",greater)

'''51.Create two matrices of shape 3x4 and perform:
addition,multiplication'''
# import numpy as np
# random_array=np.random.randint(1,20,(3,4))
# random_array1=np.random.randint(1,10,(3,4))
# addition=random_array+random_array1
# multiplication=random_array*random_array1
# print("Addition:",addition)
# print("Multiplication:",multiplication)

'''52.Create a random_arr and extract the diagonal elements.'''
# import numpy as np
# random_array=np.random.randint(1,20,(4,4))
# diagonal=np.diagonal(random_array)
# print(random_array)
# print("Diagonal:",diagonal)

'''53.Create a random_arr and calculate the mean of each column and each row.'''
# import numpy as np
# random_array=np.random.randint(1,20,(4,4))
# print(random_array)
# mean_column=random_array.mean(axis=0)
# mean_row=random_array.mean(axis=1)
# print("Mean of column:",mean_column)
# print("Mean of rows:",mean_row)

'''54.Create a random 5x5 random_arr and sort each row and each column.'''
# import numpy as np
# random_array=np.random.randint(2,30,(5,5))
# print(random_array)
# print("\n")
# sort_row=np.sort(random_array,axis=1)
# sort_column=np.sort(random_array,axis=0)
# print(sort_row)
# print("\n")
# print(sort_column)

'''55.Create a random_arr and flatten it into 1D array.'''
# import numpy as np
# random_array=np.random.randint(2,30,(2,3))
# print(random_array)
# flattent=random_array.flatten()
# print("Flattent:",flattent)

'''56.Create a large random_arr (100x100) and compute its total sum.'''
# import numpy as np
# random_array=np.random.randint(2,30,(100,100))
# print(random_array)
# total=random_array.sum()
# print("Total sum:",total)

'''57.Transpose the random_arr an array from 1 to 12 using np.arange().Print its new shape.'''
# import numpy as np
# random=np.random.randint(1,12,(2,2))
# print(random)
# transpose=random.T
# print("Transpose")
# print(transpose)

'''58.Transpose that column vector.'''
# import numpy as np
# random_array=np.random.randint(2,30,(3,1))
# print(random_array)
# print("Transpose the column vector")
# transpose=random_array.T
# print(transpose)

'''59.A =
[[1,2],
 [3,4]]
B =
[[5,6],
 [7,8]]
Multiply random_arr A and B element-wise.'''
# import numpy as np
# a=np.array([[1,2],
# [3,4]])

# b=np.array =([[5,6],
# [7,8]])
# multiply_element_wise=a*b
# print("Multiply:",multiply_element_wise)

'''60.Transpose the random random_arr. and find it's maximum and minimum value of each rows an column
'''
# import numpy as np
# random_array=np.random.randint(1,20,(4,4))
# print(random_array)
# transpose=random_array.T
# print("Transpose array")
# print(transpose)
# maximum_column=np.max(transpose,axis=0)
# maximum_row=np.max(transpose,axis=1)
# minimum_column=np.min(transpose,axis=0)
# minimum_row=np.min(transpose,axis=1)
# print("Maximum_column:",maximum_column)
# print("Maximum_column:",maximum_row)
# print("Minimum_column:",minimum_column)
# print("Minimum_column:",minimum_row)

'''61.Replace values greater than 40 with 0.'''
# import numpy as np
# random_array=np.random.randint(30,60,(4,4))
# print(random_array)
# random_array[random_array>40]=0
# print(random_array)

'''62.Create the following array:
[1,2,3,4,5,6,7,8]
Reverse the array using np.flip().'''
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8])
# flip=np.flip(a)
# print(flip)

'''63.Create the same array and reverse it using Python slicing.'''
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8])
# slicing=a[::-1]
# print(slicing)

'''64.Create the random_arr:
[[1,2,3],
 [4,5,6]]
Flip the entire random_arr.'''
# import numpy as np
# arr_2d=np.array([[1,2,3],
# [4,5,6]])
# flip=np.flip(arr_2d)
# print(flip)

'''65.Create the random_arr:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Reverse only the rows and column.'''
# import numpy as np
# arr=np.array([[1,2,3],
# [4,5,6],
# [7,8,9]])
# rev_only_row=np.flip(arr,axis=0)
# rev_only_column=np.flip(arr,axis=1)
# print("Row reverse")
# print(rev_only_row)
# print("Column reverse")
# print(rev_only_column)

'''66.Create a random_arr using:
np.arange(1,13).reshape(3,4)
Flip the random_arr completely also reversed only the second row.
also reverse only the third column'''
# import numpy as np
# arr=np.arange(1,13).reshape(3,4)
# print(arr)
# flip=np.flip(arr)
# print("Fliped")
# print(flip)
# print("Reversed only second row")
# arr[1] = np.flip(arr[1])
# print(arr)
# print("Reversed only third column")
# arr[:, 2]=np.flip(arr[:, 2],axis=0)
# print(arr)

'''67.Create a 5x5 random random_arr.
Reverse the middle row and second column'''
# import numpy as np
# random_arr=np.random.randint(10,30,(5,5))
# print("random array")
# print(random_arr)
# print("Reversed middle row")
# random_arr[2]=np.flip(random_arr[2])
# print(random_arr)
# print("Second column")
# # random_arr[:, 1]=np.flip(random_arr[:, 1],axis=0)
# random_arr[:,1]=np.flip(random_arr[:,1],axis=0)
# print(random_arr)

'''68.Create a 4x5 random_arr.
Flip it and verify if the sum of elements changes or not.'''
# import numpy as np
# random_arr=np.random.randint(10,30,(4,5))
# print(random_arr)
# total=random_arr.sum()
# print("Total sum of random_arr:",total)
# flipped=np.flip(random_arr)
# after_flipped=flipped.sum()
# print("Sum after flipped:",after_flipped)

'''69.Create a 3x4 random_arr.
Flip it twice using np.flip().
Check if it returns the original random_arr.'''
# import numpy as np
# random_arr=np.random.randint(10,30,(3,4))
# print(random_arr)
# flipped=np.flip(random_arr)
# print("First filp:")
# print(flipped)
# flipped2=np.flip(flipped)
# print("Second flip")
# print(flipped2)

'''70.Create a 4x4 random_arr.
Transpose it and then flip rows.'''
# import numpy as np
# random_arr=np.random.randint(10,30,(3,4))
# transpose=random_arr.T
# print("Transpose")
# print(transpose)
# flipped=np.flip(transpose,axis=0)
# print("Flipped row")
# print(flipped)

'''71.Create a 4X4 random_arr.
Flip columns and then transpose the random_arr.'''
# import numpy as np
# random_arr=np.random.randint(10,30,(3,4))
# print("Original random_arr")
# print(random_arr)
# flipped=np.flip(random_arr,axis=1)
# print("Flipped")
# print(flipped)
# transpose=flipped.T
# print("Transpose random_arr")
# print(transpose)

'''72.Generate 20 random integers between 0 and 50.
Reshape them into 4x5 random_arr.
Flip the random_arr vertically and horizontally.'''
# import numpy as np
# random_arr=np.random.randint(0,50,size=20)
# print("Random array")
# print(random_arr)
# print("Reshape the random_arr")
# reshape=random_arr.reshape(4,5)
# print(reshape)
# flip_vertically=np.flip(reshape,axis=0)
# print("flipped vertically")
# print(flip_vertically)
# flip_horizontally=np.flip(reshape,axis=1)
# print("flipped horizontally")
# print(flip_horizontally)

'''73.Extract the diagonal elements after flipping the random_arr.'''
# import numpy as np
# random_arr=np.random.randint(0,50,(4,5))
# print("Random array")
# print(random_arr)
# diagonal=np.diagonal(random_arr)
# print("Diagonal element")
# print(diagonal)

'''74.Create a 6x6 random_arr.
Flip only the last two rows and  first three columns.'''
# import numpy as np
# random_arr=np.random.randint(10,50,(6,6))
# print("Random array")
# print(random_arr)
# random_arr[-2:, :3] = np.flip(random_arr[-2:, :3])
# print("\nMatrix after flipping last 2 rows & first 3 columns:")
# print(random_arr)

'''75.Create a random 5x5 random_arr.
Find the max value before and after flipping.
Compare.'''
# import numpy as np
# random_arr=np.random.randint(10,50,(6,6))
# print("Matrix")
# print(random_arr)
# before_max=random_arr.max()
# print("Before flip maximum value")
# print(before_max)

# flipped=np.flip(random_arr)
# after_max=flipped.max()
# print("After flip maximum value")
# print(after_max)

'''76.Create a 3x4 random_arr.
Reverse each row individually using a loop.'''
# import numpy as np
# random_arr=np.random.randint(10,50,(3,4))
# print("Random random")
# for row in random_arr:
#     print(row)
# for i in range(len(random_arr)):
#     random_arr[i] = random_arr[i][::-1]

# print("\nMatrix with Reversed Rows:")
# for row in random_arr:
#     print(row)

'''77.Create a 4x4 random.
Reverse:
first row
last column
entire random
in three separate steps.'''
# import numpy as np
# random_arr=np.random.randint(10,50,(4,4))
# print("Random random")
# print(random_arr)

# random_arr[0]=np.flip(random_arr[0])
# print("First row reversed")
# print(random_arr)

# random_arr[:,-1]=np.flip(random_arr[:,-1])
# print("Last column reversed")
# print(random_arr)

# entire_flip=np.flip(random_arr)
# print("Entire flip")
# print(entire_flip)

'''78.Create a 1D array from 1 to 12 and reshape it into a 3x4 random.'''
# import numpy as np
# arr_1d=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr_1d)
# reshape=np.reshape(arr_1d,(3,4))
# print("Reshape")
# print(reshape)

'''79.Flatten the random using .flatten(),.ravel().'''
# import numpy as np
# arr_1d=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr_1d)
# flatten=arr_1d.flatten()
# print(flatten)
# ravel=arr_1d.ravel()
# print(ravel)

'''80.Modify the first element of the flattened array (using .ravel()).
Check if the original random changes.'''
# import numpy as np
# random=np.random.randint(10,20,(3,3))
# print("Original array")
# print(random)
# rav=random.ravel()
# print("Ravel")
# print(rav)
# rav[0]=88
# print("Change the first element")
# print(random)

'''81.Create a random and flatten it, then reshape it back.'''
# import numpy as np
# random_arr=np.random.randint(10,20,(3,3))
# print("Original random")
# print(random_arr)
# flat=random_arr.flatten()
# print(flat)
# reshape=np.reshape(flat,(3,3))
# print(reshape)

'''82.Create a random and reverse only the second row and third column.'''
# import numpy as np
# random_arr=np.random.randint(10,20,(3,3))
# print("Original random")
# print(random_arr)

# random_arr[1]=np.flip(random_arr[1])
# print("Reversed only second row")
# print(random_arr)

# random_arr[:,2]=np.flip(random_arr[:,2])
# print("Reversed only third column")
# print(random_arr)

'''83.Flatten that random and find the sum.'''
# import numpy as np
# random_arr=np.random.randint(10,20,(3,3))
# print("Original random")
# print(random_arr)
# flat=random_arr.flatten()
# print("Flatten random")
# print(flat)
# addition=flat.sum()
# print("Sum of the random")
# print(addition)

'''84.Create a random and extract all elements greater than 5.'''
# import numpy as np
# random_arr=np.random.randint(1,15,(3,3))
# print("Original random")
# print(random_arr)
# greater=random_arr[random_arr>5]
# print(greater)

'''85.Create two matrices and add them using broadcasting.'''
# import numpy as np
# matrix1=np.random.randint(1,15,(3,3))
# matrix2=np.random.randint(15,25,(3,3))
# print("First random")
# print(matrix1)
# print("Second random")
# print(matrix2)
# addition=matrix1+matrix2
# print("After addition")
# print(addition)

'''86.Create a random.Flip columns, then transpose it.'''
# import numpy as np
# matrix1=np.random.randint(15,25,(3,3))
# print("First random")
# print(matrix1)
# fliip=np.flip(matrix1,axis=0)
# print("Flipped")
# print(fliip)
# transpose=fliip.T
# print("After transpose")
# print(transpose)

'''87.Create a random and reshape it into a 1D array.
Then reshape it into a column vector.'''
# import numpy as np
# matrix1=np.random.randint(15,25,(3,3))
# print("First random")
# print(matrix1)
# reshape_1d=matrix1.reshape(-1)
# print("Reshape in 1D")
# print(reshape_1d)
# again_reshape=matrix1.reshape(-1,1)
# print("Column vector")
# print(again_reshape)

'''88.Create a random random.
Find unique values after flattening.'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# flattening=random.flatten()
# print("Flatten")
# print(flattening)
# unique_value=np.unique(flattening)
# print("Unique value")
# print(flattening)

'''89.Create a random and reverse its diagonal elements.'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# # diagonal=np.diagonal(random)
# # print("Diagonal element")
# # print(diagonal)
# # rev_diagonal=np.flip(diagonal)
# # print("Diagonal reverse")
# # print(rev_diagonal)


# reversed_diagonal = np.diagonal(random)[::-1]
# np.fill_diagonal(random, reversed_diagonal)
# print("\nMatrix after reversing the main diagonal:")
# print(random)

# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print("Original Matrix:")
# print(matrix)
# reversed_diagonal = np.diagonal(matrix)[::-1]
# np.fill_diagonal(matrix, reversed_diagonal)
# print("\nMatrix after reversing the main diagonal:")
# print(matrix)

'''90.Flatten the dataset and compute:
mean,standard deviation'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# flat=random.flatten()
# print("Flattent:",flat)
# print("Mean:",np.mean(flat))
# print("Standard deviation:",np.std(flat))

'''91.Flip the dataset matrix vertically.'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# flip_vertically=random.reshape((1,-1))
# print("vertically flip")
# print(flip_vertically)
# flip_horizontally=random.reshape((1,-1))
# print("Horizontally flip")
# print(flip_horizontally)

'''92.Create a matrix and normalize it by dividing by max value.'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# max_term=np.max(random)
# print("Max term:",max_term)
# normalize=random/max_term
# print("Normalize")
# print(normalize)

'''93.Create a matrix and replace values greater than mean with 0.'''
# import numpy as np
# random=np.random.randint(15,25,(3,3))
# print("Original random")
# print(random)
# mean_val = np.mean(random)
# print(f"Mean: {mean_val}")
# result = np.where(random > mean_val, 0, random)
# print(f"Result:\n{result}")

'''94.Create a matrix and extract positions using np.nonzero().'''
# import numpy as np
# matrix = np.array([
#     [0, 5, 0],
#     [3, 0, 0],
#     [0, 0, 8],
#     [1, 2, 0]
# ])
# print("Original Matrix:")
# print(matrix)
# nonzero_positions = np.nonzero(matrix)
# print("\nResult of np.nonzero(matrix):")
# print(nonzero_positions)
# coordinates = list(zip(nonzero_positions[0], nonzero_positions[1]))
# print("\nExtracted Coordinates of Non-Zero Elements (row, col):")
# for coord in coordinates:
#     print(coord)

'''95.Create a matrix and reshape it into (1, n) form and (n,1) form.'''
# import numpy as np
# matrix = np.array([[1, 2, 3], 
#                    [4, 5, 6]])
# print("Original Matrix (2, 3):\n", matrix)
# reshaped_matrix = matrix.reshape(1, -1)
# print("\nReshaped Matrix (1, n):\n", reshaped_matrix)
# print("\nNew Shape:", reshaped_matrix.shape)

# reshaped_matrix2= matrix.reshape(-1, 1)
# print("\nReshaped Matrix (n, 1):\n", reshaped_matrix2)
# print("\nNew Shape:", reshaped_matrix2.shape)

'''96.Use help() to understand np.array.
Create a 1D array and 2D array'''
# import numpy as np
# a=np.array([1,2,3,4])
# help(np.array)
# help(np.unique)

'''MSE concept'''
# import numpy as np
# pred = np.array([3,5,2])
# labels = np.array([2,5,4])
# mse = np.mean((pred - labels)**2)

'''97.Create two arrays:
pred = [1,2,3]
labels = [1,2,3]
Compute the difference (pred - labels).'''
# import numpy as np
# pred=np.array([1,2,3])
# labels=np.array([8,7,6])
# mse=np.mean((pred-labels))
# print(mse)

'''98.Using the same arrays, compute:
squared difference'''
# import numpy as np
# pred=np.array([1,2,3])
# labels=np.array([8,7,6])
# mse=np.mean((pred-labels)**2)
# print(mse)

'''99.Compute the sum of squared differences.'''
# import numpy as np
# pred=np.array([1,2,3])
# labels=np.array([8,7,6])
# mse=np.sum((pred-labels)**2)
# print(mse)

'''100.Create two arrays:
pred = np.arange(1,11)
labels = np.arange(2,12)
Compute MSE.'''
# import numpy as np
# pred = np.arange(1,11)
# labels = np.arange(2,12)
# mse=np.mean((pred-labels)**2)
# mse2=np.sum((pred-labels)//2)
# print(mse)
# print(mse2)

# 101.Find the absolute error instead of squared error.
# (Hint: use np.abs())
# import numpy as np
# pred = np.arange(1,11)
# labels = np.arange(2,12)
# absolute_error=np.abs((pred-labels))
# print(absolute_error)
# mae=np.mean(absolute_error)
# print("MAE:",mae)

'''102.Create two arrays and compute:
MSE,MAE
Compare results'''
# import numpy as np
# pred = np.arange(1,11)
# labels = np.arange(20,30)
# print("Predicate:",pred)
# print("Labels:",labels)
# mse=np.mean(np.square(pred-labels))
# mae=np.mean(np.abs(pred-labels))
# print("MSE:",mse)
# print("MAE:",mae)

'''103.Create arrays:
pred = [10,20,30]
labels = [12,18,33]
Compute error manually and using NumPy.'''
# import numpy as np
# pred = np.array([10, 20, 30])
# labels = np.array([12, 18, 33])
# mae_numpy = np.mean(np.abs(pred - labels))
# mse_numpy = np.mean(np.square(pred - labels))
# print(mae_numpy)
# print(mse_numpy)

'''104.Reshape both arrays into column vectors and compute MSE.'''
# import numpy as np
# random=np.random.randint(1,10,size=7)
# random1=np.random.randint(20,30,size=7)
# print(random)
# print(random1)
# column=random.reshape(-1,1)
# column1=random1.reshape(-1,1)
# print("First reshape:",column)
# print("Second reshape:",column1)
# mse=np.mean(np.square(column-column1))
# print(mse)

'''105.Transpose the arrays and compute MSE again.
Does result change?'''
# import numpy as np
# random=np.random.randint(1,10,size=7)
# random1=np.random.randint(20,30,size=7)
# print(random)
# print(random1)
# column=random.T
# column1=random1.T
# print("First reshape:",column)
# print("Second reshape:",column1)
# mse=np.mean(np.square(column-column1))
# print(mse)
# mae=np.mean(np.abs(column-column1))
# print(mae)

'''106.Create an array from 1 to 20.
Save it using .npy
Load it again
Verify both arrays are equal'''
# import numpy as np
# arr=np.arange(1,21)
# print(arr)
# save=np.save("sachin",arr)
# load=np.load("sachin.npy")
# print("arr:",arr)
# print("loaded:",load)
# print("equal:",np.array_equal(arr,load))

'''107.Create a 3x4 matrix.
Flatten it
Save the flattened array
Load it and reshape back to original'''
# import numpy as np
# random=np.random.randint(2,22,(3,4))
# print(random)
# flat=random.flatten()
# print(flat)
# save=np.save("flat_arr",flat)
# load=np.load("flat_arr.npy")
# print("Loaded:",load)
# reshape_back=flat.reshape((3,4))
# print("Reshape back:",reshape_back)

'''108.Create an array and save it as .csv.
Load it back.'''
# import numpy as np
# arr=np.array([2,3,4,5,6,7,8,9,3,44])
# np.savetxt("Array.csv",arr)
# loaded=np.loadtxt("Array.csv")
# print("Original:",arr)
# print("Loaded:",loaded)

'''109.[Create two arrays:
pred = [1,2,3]
labels = [2,3,4]
Save both arrays
Load them
Compute MSE']'''
# import numpy as np
# pred = [1,2,3]
# labels = [2,3,4]
# np.savez("multiple_arr",pred,labels)
# loaded=np.load("multiple_arr.npz")
# pred_loaded=loaded['arr_0']
# labels_loaded=loaded['arr_1']
# print("Loaded pred:",pred_loaded)
# print("Loaded labels:",labels_loaded)
# mse=np.mean(np.square(pred_loaded-labels_loaded))
# print(mse)

'''110.Create a matrix and save it.
Flip it
Save flipped version
Compare both'''
# import numpy as np
# random=np.random.randint(20,30,(3,4))
# print(random)
# np.save("Matrix", random)
# saved = np.load("Matrix.npy")
# flipped = np.flip(saved)
# are_equal=np.array_equal(random,saved)
# print("Are they both equal:",are_equal)

'''111.Create an array and reshape it into 2D.
Save both versions.
Question: Which one is better to store?'''
import numpy as np
array1=np.array([3,4,5,6])
print(array1)
array2=array1.reshape((2,2))
print(array2)
np.save("array1.npy",array1)
np.save("array2.npy",array2)
