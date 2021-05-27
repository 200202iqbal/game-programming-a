# Technically speaking, a Python iterator object must implement two special methods, 
# __iter__() and __next__(), collectively called the iterator protocol.

#define list
from typing import Iterable


myList = [0,1,2,3]

#get an iterator using iter()
myIter = iter(myList)
print(myIter)

#iterator through it using next()

#output 0
print(next(myIter))

#output 1 
print(next(myIter))

#next(obj) is the same as obj.__next__()

#Output 2
print(myIter.__next__())

#output 3
print(myIter.__next__())

#this will raise error,no items list
# next(myIter)

#create an iterator object from that iterable
iter_obj = iter(Iterable)

#infinite loop
while True:
    try:
        #get the next item
        element = next(iter_obj)
        #do something with element
    except StopIteration:
        # if StopIteration is raised ,break from loop
        break
