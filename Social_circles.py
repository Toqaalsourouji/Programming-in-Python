def CirclesOfFriends(n, lst):

    try:
        # Error handling for invalid input
        if n <= 0:
            raise ValueError("The number of people must be greater than zero")

        # Initialize a list to store sets representing friend circles
        circles = []

        # Iterate through each pair of friends in the list
        for a, b in lst:
            # Initialize variables to track the circles of a and b
            circle_a = circle_b = None
         
            # Find if 'a' or 'b' already belongs to any existing circle
            for circle in circles:
                if a in circle:
                    circle_a = circle
                if b in circle:
                    circle_b = circle

            # If a and b are in different circles, merge the circles
            if circle_a and circle_b:
                if circle_a != circle_b:
                    circle_a.update(circle_b)  # Merge circle_b into circle_a
                    circles.remove(circle_b)   # Remove the redundant circle

            # If a is found but not b, add b to a's circle
            elif circle_a:
                circle_a.add(b)

            # If b is found but not a, add a to b's circle
            elif circle_b:
                circle_b.add(a)

            # If neither a nor b is in any circle, create a new circle
            else:
                circles.append(set([a, b]))

        # Create a set of all people from 1 to n
        people = set(range(1, n + 1))

        # Identify people already in circles
        people_in_circles = set()
        for circle in circles:
            for person in circle:
                people_in_circles.add(person)
    
        # Find people not in any circle
        lonely_people = people - people_in_circles

        # Place lonely individuals in separate single-person circles
        if lonely_people:
            circles.append(lonely_people)
        
        # Convert sets of circles to lists for better readability
        circles_list = [list(circle) for circle in circles]    
        
        # Print each friend circle with a counter
        counter = 1
        for circle in circles_list:
            print(f"Friend Circle {counter} is {circle}")
            counter += 1

    except ValueError as e:
        print(f"Value error: {e}")

# Example Usage
CirclesOfFriends(7, [(1, 2), (2, 3), (4, 6)])
