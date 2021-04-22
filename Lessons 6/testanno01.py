def f (ham: str, eggs: str = "eggs") -> str:
    print("Annotation :" , f. __annotations__)
    print("Arguments :", ham,eggs)
    return ham + " and " + eggs

print(f("spam"))