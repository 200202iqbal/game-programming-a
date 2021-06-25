import tkinter as tk
import random as r
root = tk.Tk()
root.minsize(600,400)
root.title("JanKemPo")
root.option_add("*font",["MSゴシック",15])
can = tk.Canvas(root, bg="yellow",width=600,height=400)
can.place(x=0,y=0)
tittle = tk.Label(text="JanKemPo Game",bg="yellow",font=("MSゴシック",25))
tittle.place(x=190,y=20)

gu = tk.PhotoImage(file="Game/image/gu.png")
choki = tk.PhotoImage(file="Game/image/choki.png")
pa = tk.PhotoImage(file="Game/image/pa.png")

labelVs = tk.Label(text="VS",font=("Gil Sans MT",50),bg="yellow")
labelVs.place(x=260,y=170)
can.create_image(150,200, image=gu,tag="com")
labelCom = tk.Label(text="Computer",font=("Gil Sans MT",20),bg="yellow")
labelCom.place(x=100,y=60)
can.create_image(450,200, image=gu,tag="you")
labelYou = tk.Label(text="You",font=("Gil Sans MT",20),bg="yellow")
labelYou.place(x=430,y=60)

def hantei():
    if(com_te == you_te):
        result="Draw"
        labelResult = tk.Label(text=result,font=("Gil Sans MT",20),bg="yellow")
        labelResult.place(x=500,y=500)

    elif(com_te > you_te):
        result="Win"
        labelResult = tk.Label(text=result,font=("Gil Sans MT",20),bg="yellow")
        labelYou.place(x=500,y=500)
    else:
        result="Lose"
        labelResult = tk.Label(text=result,font=("Gil Sans MT",20),bg="yellow")
        labelYou.place(x=500,y=500)


def com_rand():
    can.delete("com")
    com_te = r.randint(1,3)

    print(com_te)
    if com_te == 1:
        can.create_image(150,200, image=gu,tag="com")
    elif com_te == 2:
       can.create_image(150,200, image=choki,tag="com") 
       
    else:
        can.create_image(150,200, image=pa,tag="com")  
        


def gu_te():
    you_te = 1
    print("GU")
    can.delete("you")
    can.create_image(450,200, image=gu,tag="you")
    com_rand()
    

def choki_te():
    you_te = 2
    print("choki")
    can.delete("you")
    can.create_image(450,200, image=choki,tag="you")
    com_rand()
    

def pa_te():
    you_te = 3
    print("PA")
    can.delete("you")
    can.create_image(450,200, image=pa,tag="you")
    com_rand()

#player control : gu
buttonGu = tk.Button(text="グー")
buttonGu.place(x=360,y=310)
buttonGu["command"] = gu_te
#player control : choki
buttonChoki = tk.Button(text="チョキ")
buttonChoki.place(x=425,y=310)
buttonChoki["command"] = choki_te
#player control : pa
buttonPa = tk.Button(text="パ")
buttonPa.place(x=500,y=310)
buttonPa["command"] = pa_te
root.mainloop()