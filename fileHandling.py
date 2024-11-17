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

# file = open("simpleFile.txt", 'w')
# file.write("Welcome to File handling in python")
file = open('simpleFile.txt')
content = file.read()
print(content)
file.close()