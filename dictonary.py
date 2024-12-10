# # Sure! In Python, a dictionary is a collection of key-value pairs. Each key is unique, and it maps to a value.
# # Dictionaries are mutable, meaning you can change them after they are created. They are also unordered,
# # so the items do not have a defined order.
# #
# # ### Creating a Dictionary
# # You can create a dictionary using curly braces `{}` or the `dict()` function.
# #
# # ```python
# # # Using curly braces
# # my_dict = {
# #     "name": "Alice",
# #     "age": 25,
# #     "city": "New York"
# # }
# #
# # # Using the dict() function
# # my_dict = dict(name="Alice", age=25, city="New York")
# # ```
# #
# # ### Accessing Values
# # You can access the values in a dictionary by using their corresponding keys.
# #
# # ```python
# # print(my_dict["name"])  # Output: Alice
# # print(my_dict["age"])   # Output: 25
# # ```
# #
# # ### Adding and Updating Items
# # You can add new key-value pairs or update existing ones.
# #
# # ```python
# # my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
# # my_dict["age"] = 26  # Updating an existing key-value pair
# # ```
# #
# # ### Removing Items
# # You can remove items using the `del` keyword or the `pop()` method.
# #
# # ```python
# # del my_dict["city"]  # Removes the key-value pair with key "city"
# # my_dict.pop("email")  # Removes the key-value pair with key "email"
# # ```
# #
# # ### Iterating Through a Dictionary
# # You can iterate through the keys, values, or key-value pairs in a dictionary.
# #
# # ```python
# # # Iterating through keys
# # for key in my_dict:
# #     print(key)
# #
# # # Iterating through values
# # for value in my_dict.values():
# #     print(value)
# #
# # # Iterating through key-value pairs
# # for key, value in my_dict.items():
# #     print(key, value)
# # ```
# #
# # ### Use Cases
# # 1. **Storing Configuration Settings**: Dictionaries are often used to store configuration settings
# for applications.
# # 2. **Counting Occurrences**: You can use a dictionary to count the occurrences of items in a list.
# # 3. **Mapping Data**: Dictionaries are useful for mapping data, such as storing user information
# # where the key is the user ID and the value is the user details.
# # 4. **Caching**: Dictionaries can be used to cache results of expensive function calls to improve performance.
# #
# # ```python
# # # Example of counting occurrences
# # words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# # word_count = {}
# #
# # for word in words:
# #     if word in word_count:
# #         word_count[word] += 1
# #     else:
# #         word_count[word] = 1
# #
# # print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
# # ```
# #
# # Dictionaries are incredibly versatile and powerful, making them a fundamental part of Python programming.
# # If you have any specific use cases in mind, feel free to ask!
#
# Absolutely! Here are some common functions and methods that can be used with dictionaries in Python:
#
# ### Common Dictionary Methods
#
# 1. **`dict.keys()`**: Returns a view object that displays a list of all the keys in the dictionary.
#    ```python
#    keys = my_dict.keys()
#    print(keys)  # Output: dict_keys(['name', 'age', 'city'])
#    ```
#
# 2. **`dict.values()`**: Returns a view object that displays a list of all the values in the dictionary.
#    ```python
#    values = my_dict.values()
#    print(values)  # Output: dict_values(['Alice', 26, 'New York'])
#    ```
#
# 3. **`dict.items()`**: Returns a view object that displays a list of dictionary's key-value tuple pairs.
#    ```python
#    items = my_dict.items()
#    print(items)  # Output: dict_items([('name', 'Alice'), ('age', 26), ('city', 'New York')])
#    ```
#
# 4. **`dict.get(key, default)`**: Returns the value of the specified key. If the key does not exist,
# it returns the default value.
#    ```python
#    age = my_dict.get("age", 0)
#    print(age)  # Output: 26
#    ```
#
# 5. **`dict.update([other])`**: Updates the dictionary with elements from another dictionary object or
# from an iterable of key-value pairs.
#    ```python
#    my_dict.update({"email": "alice@example.com"})
#    print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
#    ```
#
# 6. **`dict.pop(key, default)`**: Removes the specified key and returns the corresponding value.
# If the key is not found, it returns the default value.
#    ```python
#    email = my_dict.pop("email", "Not Found")
#    print(email)  # Output: alice@example.com
#    ```
#
# 7. **`dict.popitem()`**: Removes and returns an arbitrary (key, value) pair from the dictionary.
#    ```python
#    item = my_dict.popitem()
#    print(item)  # Output: ('city', 'New York')
#    ```
#
# 8. **`dict.clear()`**: Removes all items from the dictionary.
#    ```python
#    my_dict.clear()
#    print(my_dict)  # Output: {}
#    ```
#
# 9. **`dict.copy()`**: Returns a shallow copy of the dictionary.
#    ```python
#    new_dict = my_dict.copy()
#    print(new_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
#    ```
#
# 10. **`dict.fromkeys(seq, value)`**: Creates a new dictionary with keys from `seq` and values set to `value`.
#     ```python
#     keys = ['name', 'age', 'city']
#     new_dict = dict.fromkeys(keys, "Unknown")
#     print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
#     ```
#
# ### Use Cases
# - **Configuration Settings**: Storing and accessing configuration settings for applications.
# - **Data Mapping**: Mapping user IDs to user information.
# - **Counting Occurrences**: Counting the frequency of items in a list.
# - **Caching**: Storing results of expensive function calls to improve performance.
#
# Dictionaries are incredibly versatile and powerful, making them a fundamental part of Python programming.
# If you have any specific use cases in mind, feel free to ask!

my_dict = {
    "name":"Shahnawaz",
    "age":27,
    "region": "asia",
    "mobileNumber": 12345678
}
# print(my_dict)
# print(my_dict["region"])
# my_dict["email"] = "shahnawaz@gmail.com"
# print(my_dict)
# my_dict["name"] = "alam"
# print(my_dict)
# del my_dict["name"]
# print(my_dict)
# my_dict.pop("age")
# print(my_dict)
#
# for key in my_dict:
#     print(key)
# for value in my_dict.values():
#     print(value)
for key, value in my_dict.items():
    print(key, value)