def swapLines(fileName, lineNumber1, lineNumber2):
 try:
        filename = open('input.txt', 'r') # opening file and reading it, then closing it
        lines = filename.readlines()
        filename.close()

        
        # swapping lineNumber 1 with lineNumber 2  
        lines[lineNumber1] , lines[lineNumber2] = lines[lineNumber2] , lines[lineNumber1] 
        if lineNumber1 > len(lines) or lineNumber1 < 0 or lineNumber2 > len(lines) or lineNumber2 < 0:
                raise IndexError(f"One of the line numbers ({lineNumber1}, {lineNumber2}) is out of range.")
        
 except IndexError as e: # Like in part_a.py I am handling the case where the user enter an index out of range
    print(f"Error: {e}")

 except FileNotFoundError as e: # This exception will always be added whenever I am handling opening a txt file
    print(f"Error: {e}. The file {fileName} was not found.")
        
 outfile = 'output4.txt' # creating a file to write the output to and closing it
 outfile = open('output4.txt', 'w')
 outfile.writelines(lines)
 outfile.close()

swapLines('input.txt', 0 , 1 ) 
# Enter the file you want to read from and indicies of the 2 lines you want to swap.

