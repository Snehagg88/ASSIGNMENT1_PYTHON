main_string = input("Enter the string: ")

sub_string = input("Enter the substring : ")
print(f"The substring '{sub_string}' is",
      "present" if sub_string in main_string
      else "not present", "in the main string.")
