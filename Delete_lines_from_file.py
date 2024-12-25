def deleteLines(fileName, lineNumbers):
    """
    Delete specific lines from a file and write the result to a new output file.

    Parameters:
    fileName (str): The name of the file to modify.
    lineNumbers (int): The index of the line to delete (1-based).

    Returns:
    None
    """
    try:
        # Open the file in read mode and read all lines
        with open(fileName, 'r') as filename:
            lines = filename.readlines()

        # Check if the line number is within range before attempting to delete
        if lineNumbers > len(lines) or lineNumbers <= 0:
            raise IndexError(f"Line number {lineNumbers} is out of range.")
        
        # Delete the specified line (convert to 0-based index)
        del lines[lineNumbers - 1]

        # Write the modified content to a new output file
        with open('output3.txt', 'w') as outfile:
            outfile.writelines(lines)

    # Handle invalid line numbers
    except IndexError as e:
        print(f"Error: {e}")

    # Handle file not found errors
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")

# Example Usage
deleteLines('input.txt', 5)
# Enter the file name and the line number you want to delete.
