table = [ 
    [112, 72, 69, 97, 107, 73, 92, 76, 86, 73],
    [126, 128, 118, 127, 124, 82, 104, 132, 134, 83],
    [92, 108, 96, 100, 92, 115, 76, 91, 102, 81],
    [95, 141, 81, 80, 106, 84, 119, 113, 98, 75],
    [68, 98, 115, 106, 95, 100, 85, 94, 106, 119]
]

# Initialize an empty dictionary to store the stem-and-leaf plot
Stem_Leaf = {}

# Loop through each row and number in the table to generate the stem and leaf
for row in table:
    for number in row:
        # Calculate the stem by performing integer division by 10
        stem = number // 10  # e.g., 112 // 10 = 11 (stem)
        
        # Calculate the leaf by taking the remainder when divided by 10
        leaf = number % 10   # e.g., 112 % 10 = 2 (leaf)
        
        # Check if the stem already exists in the dictionary
        if stem not in Stem_Leaf:
            # If the stem is not present, initialize an empty list for leaves
            Stem_Leaf[stem] = []
        
        # Append the current leaf to the list corresponding to the stem
        Stem_Leaf[stem].append(leaf)

# Sort the stems and print the stem-and-leaf plot
for stem in sorted(Stem_Leaf):
    # Convert each leaf to a string and join them with spaces
    leaves = ' '.join(str(leaf) for leaf in Stem_Leaf[stem])
    
    # Print the stem and corresponding leaves in the required format
    print(f"{stem}  |   {leaves}")
