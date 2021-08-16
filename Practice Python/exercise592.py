"""exercise 5.9.2 from PythonLearn a book"""

total = 0
count = 0
average = 0
largest = None
smallest = None

while True:
    inp = input("Enter a number : ")
    try:
        inp = float(inp)
        total += inp
        count +=1
        if largest is None or inp > largest:
            largest = inp
        if smallest is None or smallest > inp:
            smallest = inp
    except:
        if inp == "done":
            print("Total : ",total)
            print("Count : ",count)
            average = total/count
            print("Average : ",average)
            print("Largest : ",largest)
            print("Smallest : ",smallest)
            break
        print("Invalid input")