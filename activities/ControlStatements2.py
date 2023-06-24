# Prompt the user to input the first number
num1 = float(input("Input the first number: "))

# Prompt the user to input the second number
num2 = float(input("Input the second number: "))

# Prompt the user to input the third number
num3 = float(input("Input the third number: "))

# Check if the numbers are in increasing order
if num1 < num2 < num3:
    print("Increasing order")
# Check if the numbers are in decreasing order
elif num1 > num2 > num3:
    print("Decreasing order")
# If neither increasing nor decreasing order
else:
    print("Neither increasing or decreasing order")
