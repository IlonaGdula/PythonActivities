# Initialize variables for the first two numbers in the series
a = 0
b = 1

# Print the first two numbers
print(a)
print(b)

# Generate and print the rest of the series
while b <= 50:
    # Calculate the next number in the series
    c = a + b

    # Print the next number
    print(c)

    # Update variables for the next iteration
    a = b
    b = c
