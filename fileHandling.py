# File handling is an essential part of any programming language. In Python, it’s quite straightforward and powerful. Here’s a detailed tutorial on how to handle files in Python, covering the basics as well as some advanced concepts.
#
# 1. Opening a File
# You can open a file using the open() function. This function takes two parameters: the filename and the mode.
#
# Modes:
# 'r' - Read mode (default): Opens a file for reading.
#
# 'w' - Write mode: Opens a file for writing (creates a new file or truncates the existing file).
#
# 'a' - Append mode: Opens a file for appending (creates a new file if it doesn't exist).
#
# 'b' - Binary mode: Used with other modes to open a file in binary mode (e.g., 'rb', 'wb').
#
# file = open("simpleFile.txt", 'w')
# file.write("Welcome to File handling in python")
# File Context Managers
# Using a with statement is a best practice for file handling. It ensures that the file is properly closed after its suite finishes, even if an exception is raised.
#
# Example:
# python
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# # No need to explicitly close the file


# Reading file
# file = open('simpleFile.txt')
# content = file.read()
# print(content)
# file.close()

# #writing file
# file = open('simpleFile.txt', 'r')
# file.write("This is a new line \n")
#
# file = open('simpleFile.txt', 'r')
# print(file.read())
# file.close()

# with open('simpleFile.txt', 'r') as file:
#     print(file.read())

# using with for file opening so i don't need to close the file
with open('simpleFile.txt', 'w') as file:
    file.write("overwriting the original line \n")

with open('simpleFile.txt', 'r') as file:
    print(file.read())

# using try block to manage any exceptions with regards to file handling
try:
    with open('simpleFile1.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found please check the file name and path")