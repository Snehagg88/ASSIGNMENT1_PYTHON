import string
def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translation table to remove punctuation from the input string
    return input_string.translate(translator)

# Example usage
input_string = "Hello, world! This is a test string."
clean_string = remove_punctuation(input_string)
print(clean_string)  # Output: Hello world This is a test string
