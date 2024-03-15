FILE_NAME = "my_file.txt"

# Function to write to the file
def write_to_file():
    try:
        with open(FILE_NAME, 'w') as file:
            file.write("this is a script.\n")
            file.write("it is a file reading script.\n")
            file.write("it is also supposed to display the file's contents.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File writing process completed")

#Function to read from the file
def read_from_file():
    try:
        with open(FILE_NAME, 'r') as file:
            print("File contents:")
            print(file.read())
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File reading process completed.")

# Function to append to the file
def append_to_file():
    try:
        with open(FILE_NAME, 'a') as file:
            file.write("\nThis is the first line to be appended after the file was created.\n")
            file.write("This line followed suit.\n")
            file.write("You get where I'm going with this.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending process completed.")

# Main function
def main():
    write_to_file()
    read_from_file()
    append_to_file()

# Call the main function
if __name__ == "__main__":
    main()