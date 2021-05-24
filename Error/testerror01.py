#while True print("Hello world") #test error sintaks

#x  = 10 * (1/0) #ゼロ割 / pembagian 0
#spam = 5
#x = 4 + spam * 3
#y = "2" + 2

while True:
    try:
        x = int(input("Please enter: "))
        break
    except (RuntimeError,TypeError,NameError):
        pass
    except ValueError: #percobaan 
        print("Try again 2")   
    except ValueError:
        print("Try again")
 
    