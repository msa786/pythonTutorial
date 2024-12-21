# Simple program to understand for loop
# for i in range(5):
#     print("Iteration number:", i)

lists = [1, 2, 3, 4, 5]
# for element in lists:
#     print(element)

# # program to print even number
# for num in lists:
#     if num % 2 == 0:
#         print(num)
# program to add all the numbers in the lists
# sum = 0
# for num in lists:
#     sum += num
# print("The sum of the numbers is - ",sum)

#program to iterate items in dictionary
dict = {'name': 'Shahnawaz', 'age': 21, 'city': 'kolkata'}
for key in dict:
    print(key, ":", dict[key])

#program to iterate over items and keys using .items() generators
dict = {'k1': 'value1', 'k2':'value2', 'k3':'value4'}
for key, value in dict.items():
    print(key,value)