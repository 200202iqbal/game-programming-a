#自分の生年月日
birth = 1995,12,13
stringBirth = ""
for i in birth:
    stringBirth += str(i)
    stringBirth += " / "

print("My birthday is", stringBirth[0:-2])

#2
birth = [2000,1,2]
print("My Birthday is ", end =" ")
cnt = 0
for i in birth:
    print(i, end =" ")
    if cnt < 2:
        print("/",end =" ")
    cnt +=1
print()