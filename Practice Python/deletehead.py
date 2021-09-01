def delete_head(t):
    del t[0]

letters = ["a","b","c","d"]
delete_head(letters)
print(letters)

t1 = [1,2]
t2 = t1.append(3) #just modify list not create a new list
print(t1)
print(t2)

t3  = t1 + [3] #create a new list
print(t3)

def tail(t):
    return t[1:]

t4 = tail(t3)
print(t4)
print(t3)

fruits = ["apple","strawberry","alpukat","orange","watermellon"]

def chop(list):
    list[0] = None
    list[-1] = None
    return list

def middle(list):
    newList = list[1:-1]
    return newList


print(chop(fruits))
print(middle(fruits))