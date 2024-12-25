# Run-Length Encoding (RLE) - Encoder
def rle_encode(line):
    # Return a space if the input string is empty
    if not line:
        return " "
    
    # Initialize an empty list to store encoded results
    encode = [] 
    # Start by tracking the first character
    character = line[0]
    count = 0

    # Iterate over each character in the input string
    for char in line:
        # If the current character matches the tracked character, increment the count
        if char == character:
            count += 1
        else:
            # If the character changes, append the current character and count to the encoded list
            encode.append(f"{character}/{count}")
            # Update to track the new character
            character = char
            count = 1

    # Append the final character run to the encoded list (important to avoid missing last sequence)
    encode.append(f"{character}/{count}")
    
    # Join the encoded parts into a single string separated by spaces
    return ' '.join(encode) 


# Run-Length Encoding (RLE) - Decoder
def rle_decode(encode):
    # Return a space if the encoded string is empty
    if not encode:
        return " "
    
    # Split the encoded string into parts based on spaces
    parts = encode.split() 
    # Initialize an empty string to store the decoded result
    decode = ''

    # Iterate over each encoded part (e.g., 'a/3', 'b/2')
    for part in parts:
        # Split each part by '/' to extract character and its count
        character, count = part.split('/')
        # Reconstruct the original string by repeating the character by its count
        decode += character * int(count) 

    # Return the fully decoded string
    return decode 


# I/O Handling
# Encode a sample string
encode = rle_encode("aaabbcccc33335555511")
print("Encode:", encode)

# Decode a sample encoded string
decode = rle_decode("a/3 b/2 c/4 3/4 5/5 1/2")
print("Decode:", decode)
