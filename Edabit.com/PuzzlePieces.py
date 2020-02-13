"""
    Write a function that takes two lists and adds the first element 
    in the first list with the first element in the second list, 
    the second element in the first list with the second element in the second list, etc, etc. 
    Return True if all element combinations add up to the same number. Otherwise, return False.
"""
def puzzle(a1,a2):
    mytemp = [] 
    if(len(a1) != len(a2)):
        return False
    for a,b in zip(a1,a2):
        final = a + b
        mytemp.append(final)    
    return True if mytemp.count(mytemp[0]) == len(mytemp) else False

alpha = [1,2,3,4,5]
beta = [5,4,3,2,7]
print(puzzle(alpha,beta))