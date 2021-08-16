word = str(input())

vowel = ["a","i","u","o","e"]

rule = len(word) >= 1 and len(word) <= 10
if rule:
    for v in vowel:
        word = word.replace(v,"")
    print(word)

def removeVowel(word):
    vowel = ["a","i","u","e","o"]
    word = word.lower()
    for v in vowel:
        word = word.replace(v,"")
    word = word.capitalize()
    return word

newWord = "Iqbal"
print(removeVowel(newWord))
