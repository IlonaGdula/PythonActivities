# Function to calculate the factorial of a number
def factorial(n):
    # Check if the number is negative
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Initialize the factorial variable
    fact = 1

    # Compute the factorial
    for i in range(1, n + 1):
        fact *= i

    return fact

# Test the factorial function
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print("The factorial of", num, "is", result)
