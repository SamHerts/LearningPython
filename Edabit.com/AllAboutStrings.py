"""
    Create a function that, given a string with at least 
    three characters, returns an array of its:

    1. Length.
    2. First character.
    3. Last character.
    4. Middle character, if the string has an odd number of characters. 
        Middle TWO characters, if the string has an even number of characters.
    5. Index of the second occurrence of the second character in the 
        format "@ index #" and "not found" if the second character doesn't occur again.
"""
def all_about_strings(str):
    lst = list(str)
    ln = len(lst)
    first = lst[0]
    last = lst[ln-1]
    mid = lst[ln//2] if ln%2!=0 else lst[ln//2-1]+lst[ln//2]
    index = "@ index {}".format(lst.index(lst[1], 2,ln)) if lst[1] in lst[2:] else "not found"
    return [ln,first,last,mid,index]

print(all_about_strings("LASA"))
print(all_about_strings("Computer"))
print(all_about_strings("Science"))