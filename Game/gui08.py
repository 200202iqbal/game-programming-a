import tkinter
root = tkinter.Tk()
root.minsize(600,400)
root.title("Test Window")
can = tkinter.Canvas(bg="black",width="500",height="300")
can.place(x=0,y=0)
img = tkinter.PhotoImage(file="image/cat.png")
can.create_image(150,100,image=img)
root.mainloop()