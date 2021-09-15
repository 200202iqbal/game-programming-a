from tkinter import *
from tkinter import ttk

#ボタン１
def dvd_clicked():
    button1.state(["pressed"])
    button2.state(["!pressed"])
    s.set("DVD clicked.")

#ボタン2
def download_clicked():
    button1.state(["!pressed"])
    button2.state(["pressed"])
    s.set("Download clicked")


root = Tk()
root.title("Button Example")

#Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=(10)
)

frame1.grid()

icon1 = PhotoImage(file="asset/downloadbutton.png")
button1 = ttk.Button(
    frame1,
    image=icon1,
    text="DVD",
    compound=TOP,
    padding=(10),
    
    command=dvd_clicked)

button1.grid(row=0,column=0)

icon2 = PhotoImage(file="asset/diskbutton.png")
button2 = ttk.Button(
    frame1,
    image=icon2,
    text="Download",
    compound=TOP,
    padding=(20),
    
    command=download_clicked
)

button2.grid(row=0,column=1)

#ラベル
s = StringVar()
label1 = ttk.Label(
    frame1,
    textvariable=s
)
label1.grid(row=1,column=0,columnspan=2)
root.mainloop()