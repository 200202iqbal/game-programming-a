"""To find the largest value in a list or sequence"""

largest = None
print("Before : ",largest)
for itervar in [3,41,21,9,74,15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop : ", itervar,largest)
print("Largest :",largest)

def maximum(a):
    largest = None
    """A method to find the largest value in a list or sequence"""
    for itervar in a:
        if largest is None or itervar > largest:
            largest = itervar
    return largest

a = [1,22,44,55,66,77,99,100,105,3,2]
print("Largest : ",maximum(a))

def minimum(a):
    smallest = None
    """A method to find the smallest value in a list or sequence"""
    for itervar in a:
        if smallest is None or itervar < smallest:
            smallest = itervar
    return smallest

print("Smallest : ", minimum(a))