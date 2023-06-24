def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Check for divisibility from 2 to square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
