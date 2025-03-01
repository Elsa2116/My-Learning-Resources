import random

print("""
Please Select Operation:
1. Add
2. Subtract
3. Multiply
""")

# Get user choice
choice = int(input("Select operation from 1, 2, or 3: "))

# Validate user input
if choice not in (1, 2, 3):
    print("Invalid Choice")
    random.exit()

# Get user input for numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

# Perform operation based on choice
if choice == 1:
    result = a + b
elif choice == 2:
    result = a - b
else:  # choice == 3
    result = a * b

# Display result
print("Result is:", result)