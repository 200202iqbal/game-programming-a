s = input()
list = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
if(s.isdecimal()):
    s=int(s)
    print(list[s])
elif(s=="A"):
    s = 10
    print(list[s])
elif(s=="B"):
    s = 11
    print(list[s])
        
    