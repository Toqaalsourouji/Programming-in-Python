def replaceLines(fileName, lineNumbers, newStrings):
    """
    Replace multiple specific lines in a file with new strings.

    Parameters:
    fileName (str): The name of the file to modify.
    lineNumbers (list): List of line numbers to replace (1-based).
    newStrings (list): List of new strings to replace at the specified lines.

    Returns:
    None
    """
    try:
        # Open the file in read mode and read all lines
        with open(fileName, 'r') as filename:
            lines = filename.readlines()

        # Iterate over lineNumbers and replace lines with newStrings
        for i, lineNumber in enumerate(lineNumbers):
            # Check if line number is valid
            if lineNumber > len(lines) or lineNumber <= 0:
                raise IndexError(f"Line number {lineNumber} is out of range.")
            
            # Replace the line (convert to 0-based index)
            lines[lineNumber - 1] = newStrings[i] + '\n'
        
        # Write the modified content to a new output file
        with open('output2.txt', 'w') as outfile:
            outfile.writelines(lines)
    
    # Handle invalid line numbers
    except IndexError as e:
        print(f"Error: {e}")
    
    # Handle file not found error
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")

# Example Usage
replaceLines(
    'input.txt', 
    [2, 9], 
    ['My name is Toqa', 'I have a dog.']
)
