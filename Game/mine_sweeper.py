### mine sweeper ###
import pygame
import sys
from pygame.locals import QUIT,MOUSEBUTTONDOWN
from random import randint
from math import floor

#横に20マス
WIDTH = 20
#縦に15マス
HEIGHT = 15
#マスのサイズは50ピクセル
SIZE = 50
#爆弾の数は20
NUM_OF_BOMBS = 20
#マスの状態
EMPTY=0
BOMB=1
OPENED=2
#開いたマスの数
OPEN_COUNT=0
#マスのチェック
CHECKED=[[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


pygame.init()
SURFACE = pygame.display.set_mode((WIDTH*SIZE,HEIGHT*SIZE))
FPSCLOCK = pygame.time.Clock()

def main():
    #フォントの設定
    smallfont = pygame.font.SysFont(None,36)
    largefont = pygame.font.SysFont(None,72)
    #メッセージの設定
    message_clear = largefont.render("!!CLEARED!!",True,(0,255,255))
    message_over = largefont.render("!!GAME OVER!!",True,(0,255,255))
    #メッセージの四角形の情報を取得
    message_rect = message_clear.get_rect()
    #メッセージの四角形を画面の中央にセット
    message_rect.center = (WIDTH*SIZE/2,HEIGHT*SIZE/2)  
    #ゲームオーバーフラグにFalseをセット
    game_over = False
    #フィールドの設定
    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]
    #爆弾の配置
    count = 0
    while count < NUM_OF_BOMBS:
        xpos,ypos = randint(0,WIDTH-1),randint(0,HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count +=1
        #print(field)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #マウスの左ボダンが押されたら
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                #クリックされたタイルんｐ座標を取得
                xpos = floor(event.pos[0]/SIZE)
                ypos = floor(event.pos[1]/SIZE)
                #クリックされたタイルが爆弾なら
                if field[ypos][xpos] == BOMB:
                    #ゲームオーバー
                    game_over = True
                #爆弾でなければ
                else:
                    open_tile(field,xpos,ypos)
        SURFACE.fill((0,0,0))
        #フィールドの描画
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE,ypos*SIZE,SIZE,SIZE)
                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE,(192,192,192),rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE,(255,255,0),rect)

        #線の描画
        for index in range(0,WIDTH *SIZE, SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(index,0),(index,HEIGHT*SIZE))
        
        for index in range(0,HEIGHT*SIZE,SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(0,index),(WIDTH*SIZE,index))
        
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()