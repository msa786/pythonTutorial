# **Practical Example of the `pass` Statement in Python**
#
# **Scenario:**
#
# Let's imagine you're building a text-based adventure game. You've outlined the basic structure, but you haven't yet implemented the specific actions for each room. In this case, you can use the `pass` statement as a placeholder to ensure the code runs without errors, even though the functionality is incomplete.
#
# **Code Example:**
#
# ```python
def room1():
    print("You're in a dimly lit room.")
    print("There's a door to the north and south.")

    action = input("What do you do? (north/south/quit): ")

    if action == "north":
        # Placeholder for future implementation
        pass
    elif action == "south":
        # Placeholder for future implementation
        pass
    elif action == "quit":
        print("Goodbye!")
        quit() #for quiting the program here
    else:
        print("Invalid action.")

# Main game loop
while True:
    room1()


# **Explanation:**
#
# 1. **Placeholder in Function:**
#    - Inside the `room1` function, the `if` and `elif` blocks use `pass` as a placeholder for the actual actions that will be implemented later.
#    - This prevents a `SyntaxError` as Python requires at least one statement within a block.
#    - The `pass` statement essentially tells Python to do nothing, allowing the code to execute without errors.
#
# 2. **Maintaining Code Structure:**
#    - Using `pass` helps maintain the overall structure of the code, even when parts of it are still under development.
#    - This makes it easier to add functionality later without affecting the existing code.
#
# **Key Points:**
#
# - **Avoiding Syntax Errors:** `pass` prevents errors when you have a block of code that needs to be filled in later.
# - **Placeholder for Future Implementation:** It's a temporary solution to keep the code running while you work on the actual logic.
# - **Maintaining Code Readability:** Using `pass` can make your code more readable by indicating where you plan to add more functionality.
#
# By using the `pass` statement strategically, you can create well-structured and maintainable Python code, even when it's in its early stages of development.
