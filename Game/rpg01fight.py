### rpg01fight ###
import tkinter as tk
import random
import time
 
class FightManager():
    def __init__(self):
        self.dialog = tk.Frame(width=820,height=434)
        self.dialog.place(x=10,y=10)
        self.can = tk.Canvas(self.dialog,width=820,height = 434)
        self.can.place(x=10,y=10)
        self.can.create_rectangle(0,0,600,434, fill ="black")
        self.fbut = tk.Button(self.dialog, text="攻撃")
        self.fbut.place(x = 180,y = 340)
        self.fbut["command"] = self.click_fight
        self.rbut = tk.Button(self.dialog, text="力を貯める")
        self.rbut.place(x = 320,y = 340)
        self.rbut["command"] = self.click_reserve
        self.images = [tk.PhotoImage(file ="image/big_t.png"),
                       tk.PhotoImage(file ="image/little_t.png")]
        
        self.can.create_image(180,160,image = self.images[0])
        self.lbl = tk.Label(self.dialog,text = "ラベル",fg="white",bg="black",justify="left")
        self.lbl.place(x=360,y=10)
        self.dialog.place_forget()

    def fight_start(self,map_data,x,y,brave):
        self.dialog.place(x=10,y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
        self.brave = brave
        p = self.map_data[y][x]
        self.can.delete("all")
        self.can.create_rectangle(0,0,620,434,fill="black")
        self.can.create_image(180, 160 , image=self.images[p - 5])
        self.lbl["text"] = ""
        if p == 5:
            self.monster =Monster1()
        elif p == 6:
            self.monster=Monster2()
        self.lbl["text"] = self.monster.name + "が表れだ"
    
    def click_fight(self):
        self.do_turn(self.brave.get_atk())
    def click_reserve(self):
        self.do_turn(-1)
    def do_turn(self,brave_atk):
        monster_dfs = self.monster.get_dfs()
        if brave_atk < 0:
            lbltext = "勇者（ゆうしゃ)は力(ちから)をためた"
        else:
            lbltext = "勇者の攻撃"
            self.lbl["text"] = lbltext
            self.dialog.update()
            time.sleep(2)
            dmg =  brave_atk - monster_dfs
            self.monster.culc_hp(brave_atk,monster_dfs)
            if dmg <=0:
                lbltext = lbltext + "\n 防がれた"
            else:
                lbltext = lbltext + "\n" + str(dmg) + "のダメージを与えた"
        self.lbl["text"] =lbltext
        self.dialog.update()
        time.sleep(2)
        lbltext = lbltext + "\nモンスターの残り体力は " + str(self.monster.hp)
        self.lbl["text"] = lbltext
        self.dialog.update()
class Character:
    def __new__(cls):
        obj = super().__new__(cls)
        obj.rsv = 1
        return obj
    def reserve(self):
        self.rsv = self.rsv + 1
    def get_atk(self):
        r = self.rsv
        self.rsv = 1
        return random.randint(1,self.atk * r)
    def get_dfs(self):
        return random.randint(1,self.dfs)
    def culc_hp(self,atk,dfs):
        dmg = atk - dfs
        if dmg < 1:
            return self.hp
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

class Brave(Character):
    def __init__(self):
        self.name = "勇者"
        self.hp = 30
        self.atk = 15
        self.dfs = 10

class Monster1(Character):
    def __init__(self):
        self.name = "モンスター1"
        self.hp = 20
        self.atk = 15
        self.dfs = 5

class Monster2(Character):
    def __init__(self):
        self.name ="モンスター2"
        self.hp = 10
        self.atk = 8
        self.dfs = 5