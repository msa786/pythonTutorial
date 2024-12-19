# Find your generation
while True:
    print("Welcome to find your generation game")
    print("Enter 1 to exit")
    try:
        year = int(input("enter your birth year:"))
    except ValueError:
        print("Invalid input, try again")
        continue

    if year == 1:
        quit()
    elif 1997 <= year <= 2005:
        print("Congratulation! you are a Gen Z")
    elif 2006 <= year <= 2014:
        print("Congratulation! you are a Gen Y")
    else:
        print("Sorry your generation does not fall in any of the categories")