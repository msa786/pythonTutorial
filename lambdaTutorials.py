def demonstrate_lambdas():
    """
    This function demonstrates the usage of lambda expressions in Python.
    """

    # Example 1: A simple lambda function to add two numbers
    add = lambda x, y: x + y
    print("Addition using lambda (5 + 3):", add(5, 3))

    # Example 2: A lambda function to square a number
    square = lambda x: x ** 2
    print("Square of a number using lambda (4):", square(4))

    # Example 3: Using lambda with filter to get even numbers
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers using lambda:", even_numbers)

    # Example 4: Using lambda with map to double each number
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print("Doubled numbers using lambda:", doubled_numbers)

    # Example 5: Sorting a list of tuples using a lambda as a key
    tuples = [(1, 'one'), (3, 'three'), (2, 'two')]
    sorted_tuples = sorted(tuples, key=lambda x: x[0])
    print("Tuples sorted by the first element using lambda:", sorted_tuples)


demonstrate_lambdas()
# simple square lambda example
square = lambda x: x ** 2
print(square(5))