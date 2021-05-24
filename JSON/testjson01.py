import json
#print(json.dumps([1,"simple","list"]))
x = json.dumps([1,"simple","list"])

with open("workfile03.txt" , "w") as f:
    #w > write
    json.dump(x,f)
    #json.dump([2,"word","hello"],f)

with open("workfile03.txt","r") as f:
    y = json.load(f)
    print(y)