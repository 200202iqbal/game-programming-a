times = int(input("Please enter times: "))
iteration = 0
listwords = []
while ( iteration < times ):
    words = input("Please enter a word: ")
    iteration +=1
    listwords.append(words)
print(listwords)

#2
kaisu = int(input("Please enter times: "))
lst = []
for i in range(kaisu):
    tango = input("Please enter a word:")
    lst.append(tango)
print(lst)

#underscore bisa digunakan untuk for
#for _ in range(kaisu)