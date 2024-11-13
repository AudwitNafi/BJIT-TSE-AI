# Custom exception for invalid data in the file
class InvalidDataError(Exception):
    pass

def calculate_reciprocal(file_path):
    try:
        # Try to open the file
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    # Attempt to convert each line to an integer
                    number = int(line.strip())
                    
                    # Attempt to calculate the reciprocal
                    result = 1 / number
                    print(f"The reciprocal of {number} is {result:.2f}")
                
                except ValueError:
                    # Handle non-integer data in the file
                    raise InvalidDataError(f"Invalid data found in file: '{line.strip()}' is not an integer")
                
                except ZeroDivisionError:
                    # Handle division by zero
                    print("Error: Division by zero is not allowed")

    except FileNotFoundError:
        # Handle case where the file does not exist
        print(f"Error: The file '{file_path}' was not found.")
    
    except InvalidDataError as data_error:
        # Catch any invalid data errors raised within the file processing
        print(data_error)
    
    except Exception as general_error:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {general_error}")

    finally:
        # Final cleanup or status report
        print("File processing complete.")

# Example usage
calculate_reciprocal(r"c:\Users\BJIT\Desktop\test.txt")