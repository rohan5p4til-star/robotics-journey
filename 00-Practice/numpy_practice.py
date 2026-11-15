import numpy as np
import math

# #arrays

#  difference between numpy and python is that when we view b we get first three items in array a but when we change the first item into something else for b it also changes that value for array a as well
 a=np.array([1,2,3,4,5])
 b = a[:3]
 b[0] = 4
 print(a)
 print(b)

#Two- and higher-dimensional arrays can be initialized from nested Python sequences:
a1= np.array([[1,2,3],[1,2,3],[2,2,2]])
print(a1)
print(a1[0, 0])

# #array attributes

#ndim- dimension of the array
print(a1.ndim)
print(a.ndim)

#shape
print(a1.shape)
print(len(a.shape) == a.ndim)

#size
print(a1.size)
print(a1.size == math.prod(a1.shape))

#dtype: arrays can only have one datatype; dtype will tell us what that type is 
print(a1.dtype)

#How to create a basic array

#np.zeros(): this creates an array with a certain amount of 0s   np.ones(): same idea but with ones
az = np.zeros(2)
azo = np.ones(2)
print(az)
print(azo)

#np.empty()
ae = np.empty(5)
print(ae)

#np.arange you can make an array with a range of numbers and you can also add a start number and stop number with spacing
ar=np.arange(4)
print(ar)
ars = np.arange(2, 11, 2)
print(ars)

#np.linspace:  array with values that are spaced linearly in a specified interval
als=np.linspace(0, 10, num=10)
print(als)

#you can specify the data type of the arrange 
x = np.ones(2, dtype=np.int64)
print(x)

#Adding, removing, and sorting elements

#np.sort() allows sorting of the arrays
x = np.array([1,2,3,4,9,8,7,6,5])  
print(np.sort(x))

#np.concatenate(()) allows us to combine arrays
y = np.array([1,2,3,4])
z = np.array([5,6,7,8,9])
print(np.concatenate((y,z)))
x1= np.array([[1, 2], [3, 4]])
y1 = np.array([[5, 6]])
print(np.concatenate((x1, y1)))