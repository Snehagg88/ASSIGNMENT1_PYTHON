filename = "output1_5_6.txt"
try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Print the content to the console
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")