def swapCharacters(fileName, charIndex1, charIndex2):
    """
    Swap characters at two specific indices in each line of a file and write the result to a new output file.

    Parameters:
    fileName (str): The name of the file to modify.
    charIndex1 (int): The index of the first character to swap (0-based).
    charIndex2 (int): The index of the second character to swap (0-based).

    Returns:
    None
    """
    try:
        # Open the file in read mode and read all lines
        with open(fileName, 'r') as filename:
            lines = filename.readlines()

        # Iterate over each line and perform character swapping
        for i in range(len(lines)):
            # Only perform swapping if both indices exist in the current line
            if len(lines[i]) > max(charIndex1, charIndex2):
                # Convert the line into a list to allow character swapping
                line = list(lines[i])
                
                # Swap the characters at the specified indices
                line[charIndex1], line[charIndex2] = line[charIndex2], line[charIndex1]
                
                # Rejoin the list into a string and update the line
                lines[i] = ''.join(line)
            
            # Error handling for character index out of range (post swap attempt)
            if charIndex1 >= len(lines[i]) or charIndex1 < 0 or charIndex2 >= len(lines[i]) or charIndex2 < 0:
                raise IndexError(
                    f"One of the character indices ({charIndex1}, {charIndex2}) is out of range for line {i}."
                )

        # Write the modified content to a new output file
        with open('output6.txt', 'w') as outfile:
            outfile.writelines(lines)

    # Handle invalid character indices
    except IndexError as e:
        print(f"Error: {e}")

    # Handle file not found errors
    except FileNotFoundError as e:
        print(f"Error: {e}. The file '{fileName}' was not found.")

# Example Usage
swapCharacters('input.txt', 0, 3)
# Enter the file name and the indices of the characters to swap.
# In this example, characters at index 0 and 3 will be swapped in each line.
