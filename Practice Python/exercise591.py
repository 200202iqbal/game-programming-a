"""exercise 5.9.1 from PythonLearn a book"""

total = 0
count = 0
average = 0

def checklargest(value):
    
    value = list(float(value))
    largest = None
    for i in value:
        if largest is None or i > largest:
            largest = i
    return largest

while True:
    inp = input("Enter a number : ")
    try:
        inp = float(inp)
        total += inp
        count +=1
        listval = list(total)
    except:
        if inp == "done":
            
            print("Total : ",total)
            print("Count : ",count)
            average = total/count
            print("Average : ",average)
            break
        print("Invalid input")
    

    

