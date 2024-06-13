import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def calculate_cos(x, terms):
    cos_x = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cos_x += term
    return cos_x


# User input
x = float(input("Enter the value of x (in radians): "))
terms = int(input("Enter the number of terms to use in the series: "))

# Calculate cos(x) using the series
calculated_cos = calculate_cos(x, terms)

# Calculate cos(x) using the built-in function
actual_cos = math.cos(x)

# Calculate the difference
difference = abs(calculated_cos - actual_cos)

# Display results
print(f"Calculated cos({x}) using series: {calculated_cos:.3f}")
print(f"Actual cos({x}) using math.cos: {actual_cos:.3f}")
print(f"Difference: {difference:.3f}")
