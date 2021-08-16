"""Python Learn 6.3 Traversal through a string with a loop"""

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print("------------------")
index = len(fruit)-1
while index > -1:
    letter = fruit[index]
    print(letter)
    index = index - 1

