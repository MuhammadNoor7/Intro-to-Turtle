# FizzBuzz implementation
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Calculate square and cube of a user-input number
try:
    user_input = int(input("Enter a number: "))
    square = user_input ** 2
    cube = user_input ** 3
    print(f"The square of {user_input} is {square}.")
    print(f"The cube of {user_input} is {cube}.")
except ValueError:
    print("Please enter a valid integer.")
