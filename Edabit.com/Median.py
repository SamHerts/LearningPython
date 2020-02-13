"""
    Create a function that takes a list of numbers and return its median. 
    If the input list is even length, take the average of the two medians, 
    else, take the single median.
"""

def median(lst):
    ln = len(lst)
    lst = sorted(lst)
    return lst[ln//2] if ln%2 != 0 else (lst[ln//2] + lst[ln//2 - 1])/2
        

print(median([21.4323, 432.54, 432.3, 542.4567]))