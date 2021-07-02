from rpg01fight import FightManager
import tkinter
import rpg01fight as rpgfight
def draw_map():
    for y in range(0, MAX_HEIGHT):
        for x in range(0, MAX_WIDTH):
            p = map_data[y][x]
            if p == 6:
                p = 5
            can.create_image(x * 60 + 30, y * 60 + 30, image = images[p])
    can.create_image(brave_x * 60 + 30, brave_y * 60 + 30, image = images[4], tag = "brave")

def ending():
    can.delete("all")
    can.create_rectangle(0,0,600,420,fill="black")
    can.create_text(300,200,fill ="white",font ="ＭＳ　ゴシック",
                    text="""Please insert a coin to continue...
                    Please insert a coin to continue...""")
    button_up["state"] = "disabled"
    button_down["state"] = "disabled"
    button_left["state"] = "disabled"
    button_right["state"] = "disabled"
    root.unbind("<Up>")
    root.unbind("<Down>")
    root.unbind("<Left>")
    root.unbind("<Right>")

def check_move(x, y):
    global brave_x, brave_y,flag_star
    if x >= 0 and x < MAX_WIDTH and y >= 0 and y < MAX_HEIGHT:
        p = map_data[y][x]
        if p == 1:
            return
        elif p == 3:
            flag_star = True
            map_data[y][x] = 0
            can.delete("all")
            draw_map()
        elif p == 2:
            if flag_star == True:
                ending()
                return
            else:
                return
        elif p >= 5:
            fightmanager.fight_start(map_data,x,y,brave)
        # else:
        #     return
        brave_x = x
        brave_y = y
        draw_map()

def click_button_up():
    check_move(brave_x, brave_y - 1)

def click_button_down():
    check_move(brave_x, brave_y + 1)

def click_button_left():
    check_move(brave_x - 1, brave_y)

def click_button_right():
    check_move(brave_x + 1, brave_y)

root = tkinter.Tk()
root.title("RPG風")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

can = tkinter.Canvas(root, width = 600, height = 420, bg = "black")
can.place(x = 10, y = 10)
can.create_rectangle(0, 0, 600, 420, fill = "gray", tag = "drawfield")

button_up = tkinter.Button(text = "↑")
button_up.place(x = 720, y = 150)
button_up["command"] = click_button_up

button_down = tkinter.Button(text = "↓")
button_down.place(x = 720, y = 210)
button_down["command"] = click_button_down

button_left = tkinter.Button(text = "←")
button_left.place(x = 660, y = 180)
button_left["command"] = click_button_left

button_right = tkinter.Button(text = "→")
button_right.place(x = 780, y = 180)
button_right["command"] = click_button_right

def key_up(evt):
    click_button_up()
def key_down(evt):
    click_button_down()
def key_left(evt):
    click_button_left()
def key_right(evt):
    click_button_right()

root.bind("<Up>",key_up)
root.bind("<Down>",key_down)
root.bind("<Left>",key_left)
root.bind("<Right>",key_right)

images = [tkinter.PhotoImage(file = "image/sand.png"),
          tkinter.PhotoImage(file = "image/rock.png"),
          tkinter.PhotoImage(file = "image/goal.png"),
          tkinter.PhotoImage(file = "image/star.png"),
          tkinter.PhotoImage(file = "image/char1.png"),
          tkinter.PhotoImage(file = "image/monst1.png")]

MAX_WIDTH = 10
MAX_HEIGHT = 7

#array pattern map
# 0 = sand
# 1 = rock
# 2 = goal
# 3 = star
# 4 = char1
# 5 = monster1

map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 2, 0, 6, 1, 3, 1],
            [1, 1, 6, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 5, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 6, 1],
            [1, 0, 6, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#posisi kordinat karakter
brave_x = 1
brave_y = 0

brave = rpgfight.Brave()

flag_star = False
draw_map()

fightmanager = rpgfight.FightManager()
root.mainloop()