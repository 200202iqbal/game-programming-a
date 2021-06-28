import tkinter

def draw_map():
    pass

root = tkinter.Tk()
root.title("RPG風")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

can = tkinter.Canvas(root, width = 600, height = 420, bg = "black")
can.place(x = 10, y = 10)
can.create_rectangle(0, 0, 600, 420, fill = "gray", tag = "drawfield")

images = [tkinter.PhotoImage(file = "image/sand.png"),
          tkinter.PhotoImage(file = "image/rock.png"),
          tkinter.PhotoImage(file = "image/goal.png"),
          tkinter.PhotoImage(file = "image/star.png"),
          tkinter.PhotoImage(file = "image/char1.png"),
          tkinter.PhotoImage(file = "image/monst1.png")]

MAX_WIDTH = 10
MAX_HEIGHT = 7

map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

draw_map()

root.mainloop()