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

def num_of_bomb(field,x_pos,y_pos):
    #まわりの爆弾の数を返す
    count = 0
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos,ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos]== BOMB:
                count+=1
    return count


def open_tile(field,x_pos,y_pos):
    global OPEN_COUNT
    #チェック済みのタイルなら
    if CHECKED[y_pos][x_pos]:
        #何もしない 
        return
    #クリックされたタイルをチェック済みにする
    CHECKED[y_pos][x_pos] =True
    #周りのマスの爆弾の数を調べる
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            #調べるマスの座標を取得
            xpos,ypos = (x_pos + xoffset, y_pos + yoffset)
            #調べるマスがフィールド内で何もないなら
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                #マスを開いた状態にする
                field[ypos][xpos] = OPENED
                #開いたマスの数をカウントアップ
                OPEN_COUNT +=1
                #爆弾の数を調べる
                count = num_of_bomb(field,xpos,ypos)
                #爆弾が0で自分の以外のタイルなら
                if count == 0 and not (xpos == x_pos and ypos == y_pos):
                    #open_tileを再帰呼び出し
                    open_tile(field,xpos,ypos)

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
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                #クリックされたタイルんｐ座標を取得
                xpos = floor(event.pos[0]/SIZE)
                ypos = floor(event.pos[1]/SIZE)
                #クリックされたタイルが爆弾なら
                if field[ypos][xpos] == BOMB:
                    #ゲームオーバー
                    game_over = True
                #爆弾でなければ
                #else:
                elif field[ypos][xpos] != OPENED:
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
                elif tile == OPENED:
                    count = num_of_bomb(field,xpos,ypos)
                    if count > 0:
                        num_image = smallfont.render("{}".format(count),True,(255,255,0))
                        SURFACE.blit(num_image,(xpos*SIZE + 10,ypos*SIZE+10))

        #線の描画
        for index in range(0,WIDTH *SIZE, SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(index,0),(index,HEIGHT*SIZE))
        
        for index in range(0,HEIGHT*SIZE,SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(0,index),(WIDTH*SIZE,index))
        
        #メッセージ表示
        if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear,message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over,message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()