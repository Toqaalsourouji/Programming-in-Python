String = "I am going to the Gym"

# Convert the entire string to lowercase to ensure case-insensitive counting
Lower_Case = String.lower()

# Count and print the occurrence of each letter from 'a' to 'z'
for char in range(ord('a'), ord('z') + 1):
    print(f"{chr(char)}:", Lower_Case.count(chr(char)))
