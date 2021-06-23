import tkinter
root = tkinter.Tk()
root.minsize(600,400)
root.title("Test Window")
can = tkinter.Canvas(bg="black",width="600",height="400")
can.place(x=0,y=0)
img = tkinter.PhotoImage(file="image/cat2.png")
can.create_image(300,200,image=img)
root.mainloop()