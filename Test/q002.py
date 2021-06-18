#自分の生年月日
birth = 1995,12,13
stringBirth = ""
for i in birth:
    stringBirth += str(i)
    stringBirth += " / "

print("My birthday is", stringBirth[0:-2])