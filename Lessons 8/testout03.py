#str.format()
print('We are the {} who say "{}"!'.format('knights','Ni'))

print('{0} and {1}'.format('spam','eggs'))
print('{1} and {0}'.format('spam','eggs'))

print('This {food} is {adjective}.'.format(
    food='spam',adjective='absolutely horrible'))

print('The story of {1},{0} and {other}.'.format('Bill','Manfred', other='George'))

table = {'Sjoerd' : 4127, 'Jack' :4098, 'Dcab' : 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d} '
        'Dcab: {0[Dcab]:d}'.format(table))

#table を '**' 記法を使ってキーワード引数として渡す方法もあります
#'**' キーワード引数
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1,11):
    print('{0:d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.rjust(), str.ljust() と str.center() 

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

import math
print('The value pi is %5.3f.' % math.pi) #%5  ==> lebarnya karakter huruf , 
#.3f ==> berapa angka dibelakang koma. Jika angka dibelakang koma lebih banyak daripada lebar
#yang ditentukan maka akan mengisinya.

#mode は、ファイルが読み出し専用なら 'r'
# 書き込み専用 (同名の既存のファイルがあれば消去されます) なら 'w' とします
# 'a' はファイルを追記用に開きます。
# 'r+' はファイルを読み書き両用に開きます
# 省略された場合には 'r' であると仮定します。
# 。モードに 'b' をつけるとファイルをバイナリモード (binary mode) で開き、 byte オブジェクトを読み書きします。テキストファイル以外のすべてのファイルはバイナリモードを利用するべきです。