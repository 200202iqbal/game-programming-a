word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count+1
print("count A'character : ",count)

"""exercise : Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments."""

def count(letter, search_char):
    count = 0
    """exercise : Encapsulate this code in a function named count, and gen-
    eralize it so that it accepts the string and the letter as arguments."""
    for char in letter:
        if char == search_char:
            count = count+1
    return count

letter = "google"
print("Count : ",count(letter,"o"))

