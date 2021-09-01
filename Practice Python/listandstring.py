s = "spam"
t = list(s)
print(s)
print(t)

p = "pinning for the fjords"
r = p.split()
print(r)
print(r[2])

a = "spam-spam-spam"
b = "-"
c = a.split(b)
print(c)

d = "spam spam-spam spam"
e = "-"
f = d.split(e)
print(f)

g = ["pinning","for","the","fjords"]
delimeter = " "
h = delimeter.join(g)
print(h)