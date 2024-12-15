def check_palindrome(input_str):
    """Checks if a given string is a palindrome.

    Args:
        input_str: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """

    cleaned_str = input_str.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    front = 0
    back = len(cleaned_str) - 1

    while front < back:
        if cleaned_str[front] != cleaned_str[back]:
            return False
        front += 1
        back -= 1

    return True

if __name__ == "__main__":
    user_input = input("Enter your string: ")
    if check_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")