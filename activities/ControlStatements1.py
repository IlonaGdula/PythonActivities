# Prompt the user to input the first number
num1 = float(input("Input the first number: "))

# Prompt the user to input the second number
num2 = float(input("Input the second number: "))

# Prompt the user to input the third number
num3 = float(input("Input the third number: "))

# Check if all three numbers are equal
if num1 == num2 == num3:
    print("All numbers are equal")
# Check if all three numbers are different
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different")
# If neither all are equal or different
else:
    print("Neither all are equal or different")
