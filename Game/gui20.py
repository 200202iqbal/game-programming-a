import tkinter
import random as r
cat_age = r.randint(3,8)
root = tkinter.Tk()
root.minsize(600,400)
root.title("Neko Will Answer")
root.option_add("*font",["MSゴシック",20])
can = tkinter.Canvas(bg="white",width=600,height=400)
can.place(x=0,y=0)
img = tkinter.PhotoImage(file="image/cat2.png")
can.create_image(300,200,image=img)
qst = tkinter.Label(text="僕は何歳だと思う",bg="white",font=("MSゴシック",20))
qst.place(x=10,y=10)
ent = tkinter.Entry(width=6,bd=5)
ent.place(x=340, y=90)
but = tkinter.Button(text="答える")
but.place(x=440,y=85)
def but_click():
    #print("クリック")
    val = ent.get()
    #ans["text"] = val
    cat_age = r.randint(3,8)
    print(cat_age)
    if val == str(cat_age):
        ans["text"] = "正解にゃん～"
        ans.place(x=400,y=250)

    else:
        ans["text"] = "あらあら～違うよ"
        ans.place(x=380,y=250)
    
but["command"] = but_click
ans = tkinter.Label(text="答えだよ",bg="white")
ans.place(x=420,y=250)
name = tkinter.Label(text="私は\nBishnu Nyan~",bg="yellow")
name.place(x=130,y=100)
root.mainloop()