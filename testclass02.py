class MyClass:
    """A Simple Example class"""
    i = 12345

    def f(self):
        return "hello world"
x = MyClass()

x.counter = 1 
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
print(x.f())
xf = x.f()
print(xf)