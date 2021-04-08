print("""
    -----リスト型(list)-----\n\n
    Pythonは多くの複合(compound)データ型を備えており、複数の値をまとめてるのに使われます。\n
    最も汎用性が高いのはリスト(list)で、コンマ区切の値(要素)の並びを角括弧で囲んだものとして書きあらわされます。\n
    リストは異なる型の要素を含むこともありますが、通常は同じ型の要素のみを持ちます。
""")

print(">>> squares = [1,4,9,16,25]")
print(""">>> squares
        [1,4,9,16,25]
""")

print("""
    文字列(や他の全ての組み込みのシーケンス型)のように、リストはインデックスやスライスができます。
""")

square = [1,4,9,16,25]
print(square)
square.append(125)
square.append(216)
square.append(343)
print(square)

letter = ['a','b','c','d','e','f','g']
print(letter)
letter[2:5] = ['C','D','E']
print(letter)
letter[2:5] = []
print(letter)
letter[:] = []
print(letter)

a,b= 0,1
while a < 10 :
    print(a)
    a,b = b, a+b

a,b = 0,1
while a < 1000:
    print(a,end=",")
    a,b = b, a+b

y = input("Insert number : ")
print(y)
print()

y = int(input("Insert number : "))
print(y)
print("y * 100", y* 100)