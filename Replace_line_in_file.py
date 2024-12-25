def replaceLine(fileName, lineNumber, newString):
    """
    Replace a specific line in a file with a new string.
    
    Parameters:
    fileName (str): The name of the file to modify.
    lineNumber (int): The index of the line to replace (0-based).
    newString (str): The new string to replace the line with.
    
    Returns:
    None
    """
    try:
        # Open the file in read mode and read all lines
        with open(fileName, 'r') as filename:
            lines = filename.readlines()
        
        # Check if the lineNumber is within the valid range
        if lineNumber >= len(lines) or lineNumber < 0:
            raise IndexError(f"Line number {lineNumber} is out of range.")
        
        # Replace the target line with the new string
        lines[lineNumber] = newString
        
        # Write the modified content to a new output file
        with open('output1.txt', 'w') as outfile:
            outfile.writelines(lines)
    
    # Handle the case where the file does not exist
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")
    
    # Handle invalid line numbers
    except IndexError as e:
        print(f"Error: {e}")

# Example Usage
replaceLine('input.txt', 0, 'Hello Everyone!!!\n')
# Enter the file name, line number to replace, and the new string.
