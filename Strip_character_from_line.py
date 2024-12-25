def stripLine(fileName, lineNumber, character):
    """
    Remove a specific character from a line in a file and write the result to a new output file.

    Parameters:
    fileName (str): The name of the file to modify.
    lineNumber (int): The index of the line to modify (0-based).
    character (str): The character to remove from the specified line.

    Returns:
    None
    """
    try:
        # Open the file in read mode and read all lines
        with open(fileName, 'r') as filename:
            lines = filename.readlines()
        
        # Check if the line number is within range before modifying
        if lineNumber >= len(lines) or lineNumber < 0:
            raise IndexError(f"Line number {lineNumber} is out of range.")
        
        # Replace occurrences of the character in the specified line
        lines[lineNumber] = lines[lineNumber].replace(character, '')

        # Write the modified content to a new output file
        with open('output5.txt', 'w') as outfile:
            outfile.writelines(lines)

    # Handle invalid line numbers
    except IndexError as e:
        print(f"Error: {e}")

    # Handle file not found errors
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")

# Example Usage
stripLine('input.txt', 1, 'T')
# Enter the file name, the line number (0-based), and the character to remove.
