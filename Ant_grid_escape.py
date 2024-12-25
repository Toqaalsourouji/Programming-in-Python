import random

def GridEscape(m, n):

    try: 
        # Error handling for invalid grid size
        if m <= 0 or n <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")
        
        # Initialize a 2D grid filled with '0'
        Grid = [['0' for _ in range(n)] for _ in range(m)]
        
        # Place the ant at the initial hardcoded position (row 1, column 2)
        initial_row_position = 1
        initial_column_position = 2
        Grid[initial_row_position][initial_column_position] = 'X'  # 'X' marks the starting point of the ant

        # Define possible movements (up, down, left, right) as row and column shifts
        movements_of_ant = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        # Initialize current position of the ant and step counter
        current_row_position, current_column_position = initial_row_position, initial_column_position
        count = 0
        
        # Print the initial state of the grid
        print("Initial Grid:")
        for row in Grid:
            print(" ".join(str(entry) for entry in row))

        # Ant movement loop until it reaches the boundary
        while True:
            count += 1  # Increment step count for each movement
            
            # Randomly choose the direction of movement
            D = random.choice(['up', 'down', 'left', 'right'])
            D_row, D_column = movements_of_ant[D]
            
            # Calculate new position
            new_row_position = current_row_position + D_row
            new_column_position = current_column_position + D_column
            
            # If the ant tries to move out of the grid, stop the loop
            if new_row_position < 0 or new_row_position >= m or new_column_position < 0 or new_column_position >= n:
                break

            # If the ant lands on a previously visited cell, discard the movement
            if Grid[new_row_position][new_column_position] != '0':
                count -= 1  # Do not increment step count for invalid movement
                continue

            # Mark the new position with the step count and update current position
            Grid[new_row_position][new_column_position] = str(count)
            current_row_position, current_column_position = new_row_position, new_column_position

        # Print the final state of the grid
        print("Final Grid:")
        for row in Grid:
            print(" ".join(str(entry) for entry in row))

    except ValueError as e:
        print(f"Value error: {e}")

# Simulate ant movement in a 6x6 grid
GridEscape(6, 6)
