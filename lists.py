# Python Lists are versatile and widely used data structures that allow you to store and manipulate a collection of items. Here's an overview of Python lists, including usage cases and examples of functions that operate on lists:
#
# What is a Python List?
# A Python list is an ordered collection of elements, which can be of different data types (integers, strings, floats, etc.). Lists are mutable, meaning you can modify their elements after they've been created.
#
# Creating a List
# You can create a list by enclosing elements within square brackets [], separated by commas:
#
# python
# my_list = [1, 2, 3, 4, 5]
# Common Usage Cases
# Storing Multiple Values: Lists are used to store multiple values in a single variable.
#
# Iterating Over Elements: Lists are useful for looping through elements with for or while loops.
#
# Dynamic Arrays: Lists can be resized dynamically by adding or removing elements.
#
# Storing Heterogeneous Data: Lists can store elements of different data types.
#
# Examples of Functions on Lists
# Here are some common functions and methods you can use with Python lists:
#
# Append: Adds an element to the end of the list.
#
# python
# my_list.append(6)
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
# Extend: Adds elements of another list to the end of the current list.
#
# python
# my_list.extend([7, 8, 9])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Insert: Inserts an element at a specific position.
#
# python
# my_list.insert(2, 'a')
# print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6, 7, 8, 9]
# Remove: Removes the first occurrence of an element.
#
# python
# my_list.remove('a')
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Pop: Removes and returns the element at a specific position (default is the last element).
#
# python
# last_element = my_list.pop()
# print(last_element)  # Output: 9
# print(my_list)       # Output: [1, 2, 3, 4, 5, 6, 7, 8]
# Index: Returns the index of the first occurrence of an element.
#
# python
# index = my_list.index(5)
# print(index)  # Output: 4
# Count: Returns the number of times an element appears in the list.
#
# python
# count = my_list.count(5)
# print(count)  # Output: 1
# Sort: Sorts the elements of the list in ascending order (in-place).
#
# python
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
# Reverse: Reverses the order of the list elements (in-place).
#
# python
# my_list.reverse()
# print(my_list)  # Output: [8, 7, 6, 5, 4, 3, 2, 1]
# List Comprehensions: Create a new list by applying an expression to each element in an existing list.
#
# python
# squared_list = [x**2 for x in my_list]
# print(squared_list)  # Output: [64, 49, 36, 25, 16, 9, 4, 1]
# Additional Functions
# len(list): Returns the number of elements in the list.
#
# sum(list): Returns the sum of the elements in the list.
#
# max(list): Returns the maximum element in the list.
#
# min(list): Returns the minimum element in the list.

my_list1 = [1,2,3,8,5,7,100]
print(max(my_list1))
my_list1.append(11)
print(my_list1)
my_list1.extend([100,200,300])
my_list1.sort()
print(my_list1)
my_list1.reverse()
print(my_list1)
my_list1.remove(300)
print(my_list1)
my_list1.insert(2, "hello")
print(my_list1)

