# Initial list of number words from one to ten
list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"] 

# Loop through the list and modify each element by appending " plus one" based on the index
# The first element stays "one", the second becomes "one plus one", and so on
for i in range(len(list)):
    list[i] = "one" + (" plus one" * i)

# Print the modified list after the transformation
print(list)

# Initially, the output had no spaces between "oneplus" due to direct concatenation.
# This was fixed by adding spaces during concatenation, resulting in "one plus one".
