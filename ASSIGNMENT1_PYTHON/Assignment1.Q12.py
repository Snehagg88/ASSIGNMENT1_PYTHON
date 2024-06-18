def sum_of_digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

# Example usage:
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
