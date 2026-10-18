import numpy as np

# elements = np.array([[1,2,3,4,5,6,7,8,9,10]])


# elements_multiplication = np.array([[1],
#                                    [2],
#                                    [3],
#                                    [4],
#                                    [5],
#                                    [6],
#                                    [7],
#                                    [8],
#                                    [9],
#                                    [10]])
# print(elements*elements_multiplication)



# array = np.array([[1,2,3,0.2,4,5],
#                   [6,7,8,9,10,11]])
                  
# print(np.min(array))
# print(np.max(array))
# print(np.mean(array))
# print(np.var(array))
# print(np.std(array))

# print(np.argmin(array))
# print(np.argmax(array))

# print(np.sum(array, axis = 1))


# filter = np.array([61,55,67,82,91,100,78,92])
# filterd_marks = filter[(filter>70) & (filter%2==0)]
# print(filterd_marks)

# print(filter[(filter % 2 != 0)|(filter<80)])


ages = np.array([[17,19,45,16,19,20],[99,86,43,17,19,21]])

# filter = np.where(ages > 20, ages, 0)
# print(filter)


# filterd_list = np.where((ages%2!=0)&(ages>30),ages, 0)
# print(filterd_list)



# random_numbers=  np.random.default_rng()
# array = np.array([1,2,3,4])
# random_numbers.shuffle(array)
# print(random_numbers.uniform(1,101,(5,2)))
# print(array)
# print(random_numbers.choice(array,5))

