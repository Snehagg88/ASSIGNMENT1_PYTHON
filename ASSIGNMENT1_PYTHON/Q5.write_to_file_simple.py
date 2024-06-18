user_input = input("Enter the text you want to write to the file: ")
filename = "output1_5_6.txt"
with open(filename, 'w') as file:
    file.write(user_input)
print(f"Content successfully written to {filename}")