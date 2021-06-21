#program banyaknya selisih lantai dari lantai yang ingin dituju - posisi lantai sekarang
numberloop = int(input())
currentlift = 1
liftstep = 0
total = 0
rule = numberloop >= 1 and numberloop <= 100
while(numberloop>0):
    destinationlift = int(input())
    rule2 = destinationlift >= 1 and destinationlift <=100
    if(rule and rule2):
        liftstep = abs(destinationlift - currentlift)
        currentlift = destinationlift
        total += liftstep
    numberloop -=1
    
print(total)
