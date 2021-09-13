import tkinter as tk
window = tk.Tk()
greeting  = tk.Label(text="Hello World")
greeting.pack()
inputUser = tk.Entry()
inputUser.pack()
buttonOK = tk.Button(text="Enter")
buttonOK.pack()
window.mainloop()

