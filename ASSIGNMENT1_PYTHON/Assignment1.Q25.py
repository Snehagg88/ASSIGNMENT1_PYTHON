def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dst:
                dst.write(src.read())
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
    except IOError as e:
        print(f"Error: {e}")


# Example usage:
copy_file_contents('source_25.txt', 'destination_25.txt')

