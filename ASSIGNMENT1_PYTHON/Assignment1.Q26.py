def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix


string = "Hello! Welcome to the world of Python!"
prefix = "Hello"
suffix = "world!"

starts, ends = check_prefix_suffix(string, prefix, suffix)
print(f"Starts with prefix '{prefix}': {starts}")
print(f"Ends with suffix '{suffix}': {ends}")
