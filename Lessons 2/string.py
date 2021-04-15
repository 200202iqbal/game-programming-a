print("""
Usage : thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to
""")

print(r'C:\some\name')

print('C:\some\nname')

print("First line.\nSecond line.")

print(100*"a" + "bcd")

word = "Indonesia"
print("word[0] =" + word[0])
print("word[3] =" + word[3])
print("word[-1] =" + word[-1])
print("word[-3] =" + word[-3])
print("word[0:3]" + word[0:3])
print("word[2:6]" + word[2:6])

i = 0
while i < len(word):
    
    print("\n" + word[i])
    i += 1