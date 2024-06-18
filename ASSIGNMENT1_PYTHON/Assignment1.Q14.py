lines = []

print("Enter multiple lines of input. Press Enter on an empty line to finish:")

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

print("You entered the following lines:")
for line in lines:
    print(line)
