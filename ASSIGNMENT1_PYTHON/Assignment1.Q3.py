# Ist Approach
# import the 'math' module
import math
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # print(f"The factorial of {number} is {math.factorial(number)}")

   print("The factorial of", number, "is", math.factorial(number))

# 2nd Approach
#  using a function

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
#
# number = int(input("Enter a number: "))
# print(f"The factorial of {number} is {factorial(number)}")