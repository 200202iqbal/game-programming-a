2年生の授業
ゲームプログラミング

note
change directory > cd:\python39
akan menjadi c:\Python39>python

https://docs.python.org/ja/3/tutorial

Untuk mempercepat pemuatan modul, Python menyimpan cache 
setiap modul yang dikompilasi sebagai file module.version.pyc 
di direktori __pycache__.

str() 関数は値の人間に読める表現を返すためのもの
 repr() 関数はインタープリタに読める (あるいは同値となる構文がない場合は必ず SyntaxError になるような) 表現を返すためのものです。
Fungsi repr () dimaksudkan untuk mengembalikan representasi yang dapat dibaca (atau SyntaxError jika tidak ada sintaks yang setara) di interpreter.

フォーマットする前に値を変換するのに使えます / Dapat digunakan untuk mengonversi nilai sebelum memformat

 '!a' は ascii() を、 '!s' は str() を、 '!r' は repr() を適用します:

 ! ===> エクスクラメーションマーク あるいは　びっくりマーク
 [] ===> 角括弧(かくかっこ) 

 # Operator	            Expression	    Internally
# Addition	            p1 + p2	        p1.__add__(p2)
# Subtraction	        p1 - p2	        p1.__sub__(p2)
# Multiplication	    p1 * p2	        p1.__mul__(p2)
# Power	                p1 ** p2	    p1.__pow__(p2)
# Division	            p1 / p2	        p1.__truediv__(p2)
# Floor Division	    p1 // p2	    p1.__floordiv__(p2)
# Remainder (modulo)    p1 % p2	        p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	    p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	    p1.__rshift__(p2)
# Bitwise AND	        p1 & p2	        p1.__and__(p2)
# Bitwise OR	        p1 | p2	        p1.__or__(p2)
# Bitwise XOR	        p1 ^ p2	        p1.__xor__(p2)
# Bitwise NOT	        ~p1	            p1.__invert__()

# Operator	                Expression	    Internally
# Less than	                p1 < p2     	p1.__lt__(p2)
# Less than or equal to	    p1 <= p2	    p1.__le__(p2)
# Equal to	                p1 == p2	    p1.__eq__(p2)
# Not equal to	            p1 != p2	    p1.__ne__(p2)
# Greater than	            p1 > p2	        p1.__gt__(p2)
# Greater than or equal to	p1 >= p2	    p1.__ge__(p2)