import numpy as np
import matplotlib.pyplot as plt
sales_data=np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5, 160000, 185000, 205000, 230000]
])
print("====Zomato Sales analysis====")
print("\n Sales data shape",sales_data.shape)
print("\n Sample data for lst 3 restau:",sales_data[:3])
print(np.sum(sales_data,axis=0))
yearly_total=np.sum(sales_data[:,1:], axis=0)
print(yearly_total)

min_sales=np.min(sales_data[:,1:], axis=1)
print(min_sales)

max_sales=np.max(sales_data[:,1:], axis=0)
print(max_sales)

avg_sales=np.mean(sales_data[:,1:],axis=1)
print(avg_sales)


cumsum=np.cumsum(sales_data[:,1:], axis=1)
print(cumsum)
plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum,axis=0))
plt.title("Average cumulative sales accross all restaurant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

vector1=np.array([1,2,3,4,5])
vector2=np.array([6,7,8,9,10])
print("Vector addition:",vector1+vector2)
print("\n Multiplication vector",vector1*vector2)
angle=np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
print(angle)
restaurant_types=np.array(['biryani','chinese','pizza','burger'])
vectorized_upper=np.vectorize(str.upper)
print("vectorized upper",vectorized_upper(restaurant_types))
monthly_avg=sales_data[:,1:]/12
print(monthly_avg)