def f(a,L=[]):
    L.append(a)
    return (L)

print(f(1))
print(f(2))
print(f(3))
print(f(100,[]))

print(f(50),[55,60,65,70])

def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return (L)

print(ff(1))
print(ff(2))
print(ff(100))