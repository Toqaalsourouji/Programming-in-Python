import cProfile  # Import cProfile to analyze the performance of the code


# Function to generate and print all permutations of (i, j)
def permutations(x, y):
    # Loop from 0 to x and 0 to y, printing each combination
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            print(f"({i},{j})") 


# Main function to handle user input and call permutations
def main():
    # Take user input for x and y, converting them to integers
    x = int(input("Enter x: ")) 
    y = int(input("Enter y: "))
    
    # Call the permutations function with user input
    permutations(x, y)


# Execute the main function with performance profiling
if __name__ == "__main__":  
    cProfile.run('main()')
