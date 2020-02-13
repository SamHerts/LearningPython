"""
    Given a list of boxes, create a function that returns 
    the total volume of all those boxes combined together. 
    A box is represented by a list with three elements: length, width and height.
"""
def total_volume(*boxes):
    alpha = 0
    temp = 1
    for a in boxes:        
        for b in a:            
            temp *= b            
        alpha += temp
        temp = 1
    return alpha



print("final= ", total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
