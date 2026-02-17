import numpy as np
numbers=np.array([1,2,3,4,5,6,7,8,9,10])
indices=[0,2,4]
print(numbers[indices])
where_result=np.where(numbers>5)
print("NP where",numbers[where_result])
condition_array=np.where(numbers>5,"true","false")
print(condition_array)