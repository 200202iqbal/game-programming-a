def f(a, *arguments, **keywords):
    print(a)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw," : " , keywords[kw])
    print(end=" ")

#  *arguments artinya bisa menambahkan berapapun parameter tanpa memberikan keyword(nama variabel)
# **keywords artinya bisa menambahkan berapapun parameter HARUS memberikan keyword(nama variabel)
f("aa","b","c",name = "iqbal", age = 25)

f("ab","b","c","d","e","f","g","h",name = "iqbal", age = 25,country = "indonesia")