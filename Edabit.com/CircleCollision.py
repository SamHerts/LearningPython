"""
    Create a function that returns True if the given circles are intersecting, 
    otherwise return False. The circles are given as two lists containing 
    the values in the following order:

    1. Radius of the circle.
    2. Center position on the x-axis.
    3. Center position on the y-axis.
"""
def is_circle_collision(c1,c2):
    return True if (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2 <= (c1[0] + c2[0])**2 else False
print(is_circle_collision([10, 0, 0], [10, 10, 10]))
print(is_circle_collision([1, 0, 0], [1, 10, 10]))
