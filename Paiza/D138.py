#D138:おうむ返し 
inputa = input().split()
kolom = int(inputa[0])
baris = int(inputa[1])

rule = kolom,baris >= 1 and kolom,baris<=20
if(rule):
    for b in range(baris):
        stringa = input()
        if(len(stringa) == kolom):
            print(stringa)

    
        