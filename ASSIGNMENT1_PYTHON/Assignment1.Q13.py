# first=int(input("Enter First Number: "))
# print(2024-first)

import datetime
def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age
birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("Your age is:", age)