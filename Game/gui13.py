import tkinter
root = tkinter.Tk()
root.minsize(600,400)
root.title("Test Window")

can = tkinter.Canvas(bg="white",width=600,height=400)
can.place(x=0,y=0)
img = tkinter.PhotoImage(file="image/cat2.png")
can.create_image(300,200,image=img)
qst = tkinter.Label(text="僕は何歳だと思う?",bg="white",font=("MSゴシック",20))
qst.place(x=10,y=10)
ent =tkinter.Entry(width=30,bd=3)
ent.place(x=340,y=90)
root.mainloop()