squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
sq = [x ** 2 for x in range(10)]
print(sq)

it = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
#combs = []
#for x in [1,2,3]:
#     for y in[3,1,4]:
#         if x != y:
#             combs.append((x,y))
print(it)

vec = [-4,-2,0,2,4]
#create a new list with the values doubled
print ([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
fruits = ["   banana    ","   logan   berry","passionfruit  "]
print([ff.strip() for ff in fruits])
#strip = menghapus spasi di depan kata maupun di akhir didalam list
print([(x,x**2) for x in range(6)])

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])
#algoritmanya 1. nilai dari vec satu persatu di looping
# dimasukkan ke dalam variabel elem
# 2. Selanjutnya nilai yang baru dimasukkan ke elem di looping 
# kembali dan dimasukkan nilainya ke variabel num /for num in elem
# 3. Setelah itu dimasukkan ke variabel num yg paling depan 

##################################################
from math import pi
print([str(round(pi,i)) for i in range(1,6)])
#algoritmanya 1. loop dgn nilai dari 1 sampai 6
# 2. nilainya dimasukan ke variabel i
# 3. nilai dari i dimasukan ke round(pi,i). round(pi,i) merupakan method 
#pembulatan(berapa angka nilainya dibelakang koma)
# hasil pembulatan dari round di konversikan menjadi string 

mx = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([[row[i] for row in mx] for i in range(4)])
#algoritmanya yg pertama kali dieksekusi for i in range(4)
#dikarenakan di bagian depan terdapat []
#kemudian melakukan pengulangan

listzip = list(zip(*mx))
print(listzip)

##################################
a = [-1,1,66.25,333,333,1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)