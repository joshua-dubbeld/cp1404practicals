"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When you enter without specifying a number

2. When will a ZeroDivisionError occur?
When you divide a number by zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You can add an error checking loop to prevent the user from inputting zero

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When you enter without specifying a number
# 2. When you divide a number by zero
# 3. You can add an error checking loop to prevent the user from inputting in zero
