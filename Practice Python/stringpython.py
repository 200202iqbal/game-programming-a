word = "banana"

new_word = word.upper()
print(new_word)
print(type(word))
print(dir(word))
#help(str.title)

line = "  here we go    "
print(line.strip())

#help(str.strip)
line = "Have a nice day"
print(line.startswith("have"))
print(line.startswith("Have"))

print(line.lower().startswith("h"))

print(word.count("a"))
