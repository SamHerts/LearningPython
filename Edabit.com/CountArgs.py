"""
    Create a function that returns the number of argument it was called with
"""
def num_args(*input):
    return len(input)

print(num_args("Foo", Male="Bar"))
