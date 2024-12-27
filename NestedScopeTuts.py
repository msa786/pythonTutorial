# Python program to demonstrate nested statements and scope

def nested_example():
    global_var = "I am a global variable"
    print(f"Accessing global_var from nested_example: {global_var}")

    def outer_function():
        outer_var = "I am a variable in the outer function"
        print(f"Accessing global_var from outer_function: {global_var}")
        print(f"Accessing outer_var from outer_function: {outer_var}")

        def inner_function():
            inner_var = "I am a variable in the inner function"
            print(f"Accessing global_var from inner_function: {global_var}")
            print(f"Accessing outer_var from inner_function: {outer_var}")
            print(f"Accessing inner_var from inner_function: {inner_var}")

        inner_function()
        # Attempting to access inner_var here will result in an error
        # print(inner_var)  # Uncommenting this will raise an error

    outer_function()

nested_example()
