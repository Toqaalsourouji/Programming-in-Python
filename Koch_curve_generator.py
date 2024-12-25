def koch(n):
    """
    Generate the instructions for drawing a Koch curve of order n.

    Parameters:
    n (int): The order of the Koch curve.

    Returns:
    str: A string of instructions representing the Koch curve.
    """
    # Base case: when n is 0, the curve is just a single forward move
    if n == 0:
        return 'F'  # 'F' means move forward
    
    # Recursive case: generate the curve by combining parts of lower orders
    previous = koch(n - 1)
    
    # The Koch curve of higher order is formed by combining:
    # - One copy of the previous curve
    # - A left turn ('L')
    # - Another copy of the previous curve
    # - A right turn ('R')
    # - One more copy of the previous curve
    # - A left turn ('L')
    # - A final copy of the previous curve
    return previous + 'L' + previous + 'R' + previous + 'L' + previous


# Test the function with different values of n (from 0 to 9)
for i in range(10):
    print(f"Koch curve of order {i}: {koch(i)}")
