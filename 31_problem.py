'''Generate 20 random integers between 1 and 100.
Count:
How many values are between 1-25
26-50
51-75
76-100
Do this using Boolean masking.'''
import numpy as np

num=np.random.randint(1,50,size=20)
print(num)
count_number=np.sum((num>=1) & (num<=25))
print("Number between 1-25:",count_number)

# import random
# count=0
# for i in range (20):
#     num=random.randint(1,50)
#     if 1 <= num <= 25:
#         count+=1
#     print(num)
# print("Number between 1-25:",count)