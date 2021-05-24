item = str(input())
price = int(input())

rule = price >= 1 and price <=1000 and item == "chocolate","cake"
if(rule):
    if(item=="chocolate"):
        price = price * 2
        print(price)
    else:
        price = price * 5
        print(price)