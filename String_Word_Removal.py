# Initial string provided in the question
stringA = "Hello this is a beautiful morning"

# Split the string into a list of words for easier manipulation
word = stringA.split()

# Remove the word "beautiful" from the list
word.remove("beautiful")

# Rejoin the modified list into a single string to restore normal sentence format
stringB = " ".join(word)

# Print the modified string
print(stringB)
