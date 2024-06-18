def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage
input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)

print("Character frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

# str = "Welcome to the world of Python"
# print(str.count("o"))