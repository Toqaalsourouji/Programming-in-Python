def postal_code(code):
    # Validates if the postal code follows the correct format:
    # - 7 characters long
    # - Alternating pattern of letter, digit, letter, space, digit, letter, digit (e.g., T2T 2T2)
    
    # Check if the postal code is exactly 7 characters long
    if len(code) != 7:
        return False
    
    # Check if the first character is a letter
    if not code[0].isalpha():
        return False
    
    # Check if the second character is a digit
    if not code[1].isdigit():
        return False
    
    # Check if the third character is a letter
    if not code[2].isalpha():
        return False
    
    # Check if the fourth character is a space
    if not code[3] == " ":
        return False
    
    # Check if the fifth character is a digit
    if not code[4].isdigit():
        return False
    
    # Check if the sixth character is a letter
    if not code[5].isalpha():
        return False
    
    # Check if the seventh character is a digit
    if not code[6].isdigit():
        return False
    
    # If all checks pass, return True
    return True

# Test cases for different postal codes
Postal_code = ["T2T 2T2"] 
Postal_code2 = ["LL 9L"] 
Postal_code3 = ["L9L9L9"] 
Postal_code4 = ["LTL 9L9"] 

# Validate postal codes in the list and print the results
for code in Postal_code4:
    print(code, postal_code(code))
