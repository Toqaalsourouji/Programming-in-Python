def embed(fileName, startIndex, s):
    """
    Embed a string at a specific index in the contents of a file and write the result to a new output file.

    Parameters:
    fileName (str): The name of the file to modify.
    startIndex (int): The position (0-based) at which the string should be embedded.
    s (str): The string to embed at the specified index.

    Returns:
    None
    """
    try:
        # Open the file in read mode and read all contents
        with open(fileName, 'r') as filename:
            lines = filename.read()

        # Check if the startIndex is within valid range
        if startIndex > len(lines) or startIndex < 0:
            raise IndexError(f"The start index {startIndex} is out of range.")
        
        # Slice and embed the string 's' at the specified startIndex
        modified_lines = lines[:startIndex] + s + lines[startIndex:]

        # Write the modified content to a new output file
        with open('output7.txt', 'w') as outfile:
            outfile.write(modified_lines)

    # Handle invalid index
    except IndexError as e:
        print(f"Error: {e}")

    # Handle file not found errors
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")

# Example Usage
embed('input.txt', 0, 'Good Morning ')
# The example embeds 'Good Morning ' at the start (index 0) of 'input.txt'.
