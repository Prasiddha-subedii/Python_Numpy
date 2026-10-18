import numpy as np

print(np.__version__)
# array = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,9]])
# print(array*2)
# print(type(array))
another_array = np.array([1,2,3,4])
print(another_array.ndim)
# print(array.shape)
# print(array[1,2])
# print(array[0:3:-1])
# print(array[:,1])

# Scaler arithmetic

# print(array +  1 )
# print(array ** 3)

# print(array**(1/2))

# print(np.sqrt(array))


'''' Ceil and floor '''

# example =  np.array([[1.3,2.6,3.2],
#                       [4.6,5,6.9]])
# print(example.shape)

# print(np.round(example))
# print(np.ceil(example))
# print(np.floor(example))
# print(np.pi)


# radii  =  np.array([1,2,3,4,5])

# print("The correspoding area is ", np.pi * radii ** 2)



list1 = np.array([1,2,3])
list2 = np.array([9,8,7])
print(list1+list2)

print(list2>20)

# scores = np.array([45,100,75,99,52,20])

# scores[scores<40] = 0
# print(scores)


# Broad Casting 


# array1 =  np.array([[1,2],
#                     [5,6],
#                     [9,10] ,
#                     [13,14]]
#                    )
# 4,2
# 4,1
# array2 = np.array([[1]
#                    ,[2]
#                    ,[5]
#                    ,[4]])
# print(array2.shape)
# print(array1.shape)
# print(array1*array2)