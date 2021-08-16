data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ",atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

# creating a method for passing host
def parsehost(string):
    atpos = string.find("@")
    sppos = string.find(" ",atpos)
    if(atpos == -1):
        print("Invalid input")
    host = string[atpos+1:sppos]
    return host

data = input("Input string : ")
print(parsehost(data))

# Format operator % to construct string
book = 10
print("I has %d books" %book)

# %d for decimal, %g for floating point number, %s for strings
print("In %d years I have spotted %g %s." %(3, 0.1, "camels"))