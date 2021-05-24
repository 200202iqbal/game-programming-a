class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try: 
        raise cls() #The raise statement allows the programmer to force a specified exception to occur
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")