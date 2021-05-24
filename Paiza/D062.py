import string
string.ascii_uppercase
satu,dua,tiga = input().split()
satu,dua,tiga = int(satu),int(dua),int(tiga)
if(satu,dua,tiga >= 1 and satu,dua,tiga <=10):
    if(satu+dua+tiga==10):
        i = 0
        while( i < satu):
            print(string.ascii_uppercase[i],end ="")
            i +=1
        print("")
        while(i < satu+dua):
            print(string.ascii_uppercase[i],end="")
            i+=1
        print("")
        while(i < satu+dua+tiga):
            print(string.ascii_uppercase[i],end="")
            i+=1
            