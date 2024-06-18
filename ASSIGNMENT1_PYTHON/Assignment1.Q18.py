str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1= str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

print("Sorted characters of first string:", sorted(str1))
print("Sorted characters of second string:", sorted(str2))
if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else :
    print("Strings are not anagrams")