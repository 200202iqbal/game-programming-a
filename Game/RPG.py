import tkinter as tk

root = tk.Tk()

#変数を定義
minWidth = 840
minHeight = 454
gameScreenWidth = 600
gameScreenHeight = 420

#defを定義
def draw_map():
    pass
root.minsize(width=minWidth,height=minHeight)
root.title("RPG風")
root.option_add("*font",["メイリオ",20])
canvas = tk.Canvas(root,background="black",width=gameScreenWidth,height=gameScreenHeight)
canvas.place(x=10,y=10)
canvas.create_rectangle(0,0,gameScreenWidth,gameScreenHeight,fill="gray",tag="drawfield")
images = [tk.PhotoImage(file="image/sand.png"),
          tk.PhotoImage(file="image/rock.png"),
          tk.PhotoImage(file="image/goal.png"),
          tk.PhotoImage(file="image/star.png"),
          tk.PhotoImage(file="image/char1.png"),
          tk.PhotoImage(file="image/monst1.png")
]

MAX_WIDTH = 10
MAX_HEIGHT = 7

map_date = [[1,0,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1],
]
draw_map()
root.mainloop()