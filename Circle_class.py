import math

class Circle:
    def __init__(self, center, radius):
        # Initialize circle with center (x,y) and radius
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        self.center = center

    def concentric(self, anotherCircle):
        # Check if circles share the same center
        return self.center == anotherCircle.center
        
    def intersects(self, anotherCircle):
        # Check if circles intersect by comparing center distances
        x = self.center[0] - anotherCircle.center[0]
        y = self.center[1] - anotherCircle.center[1]
        d = math.sqrt(x**2 + y**2)
        
        if d <= self.radius + anotherCircle.radius:
            print("Circles intersect")
        else:
            print("Circles don't intersect")

    def remap(self, percentage):
        # Scale the radius by a percentage
        self.radius *= 1 + percentage / 100


# Testing
circle1 = Circle((0, 0), 5)
circle2 = Circle((0, 0), 3)
circle3 = Circle((4, 0), 2)

print(circle1.concentric(circle2))  # True
circle1.intersects(circle3)         # Circles intersect
circle1.remap(10)                   
print(circle1.radius)               # 5.5
