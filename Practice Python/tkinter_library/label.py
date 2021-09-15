import tkinter as tk
window = tk.Tk()
label = tk.Label(
    text="Hello Tkinter",
    foreground = "white", #set the text color to white
    background = "black", #set the background color to black
    width=10, #set the width
    height=10 #set the height
)
label.pack()
window.mainloop()