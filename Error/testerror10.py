# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# print(bool_return())

def divide(x,y):
    try:
        rst = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("rst is ", rst)
    finally:
        print("exec_finally")

print(divide(2,1))
print(divide(2,0))
print(divide("2","1"))
