# """ - this is used to create doc string
def myFunction():
    """
    INPUT: this is a function that prints hello world and does not take any input
    :return: Nothing
    """
    print("Hello from a function")

def addNumbers(num1, num2):
    """

    :param num1: takes a parameter
    :param num2: takes a parameter
    :return: addition of two numbers
    """
    return num1 + num2

myFunction()
print(addNumbers(10, 20))
