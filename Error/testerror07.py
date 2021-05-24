#raise NameError("Hi,There") akan menghasilkan NameError
# raise ValueError("Hello")

try:
    raise NameError("HiThere")
except NameError:
    print("An exceptin flew by!")
    raise
print("abc")