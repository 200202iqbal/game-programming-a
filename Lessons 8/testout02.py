import math
print(f'The value of pi is approximately {math.pi:.5f}.')

table = {'S': 100, 'J':1000, 'D':10000}
for a,b in table.items():
    print(f'{a:5} ==> {b:10d}')

a = 100
print(f'Value of a = {a}')
print(f'Value of a = {a!r}')

b = 'aaa'
print(f'Value is {b}')
print(f'Value is {b!r}')
print(f'Value is {b!s}')