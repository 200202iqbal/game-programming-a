#tupleって値を変更できません
t = 12345,54321,"hello!"
print(t[0])
print (t)
u = t , (1,2,3,4,5)
print(u)
#t[0] = 8888 エラーになる。値を変更できません
#print(t)
empty = ()
singleton = "hello", # <-- comma
print(len(empty))
print(len(singleton)) #ketika len membaca nilai variabel yang terdapat comma, yang akan dibaca banyaknya data, bukan length
print(singleton)

t = 12345,54321,"hello!"
x,y,z = t
print(x,y,z)
