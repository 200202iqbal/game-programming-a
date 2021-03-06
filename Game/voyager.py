### voyager.py ###
import pygame
import sys
from random import randint
from pygame.constants import SCRAP_BMP
from pygame.locals import QUIT, KEYDOWN, KEYUP,K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800,800))
FPSCLOCK = pygame.time.Clock()

def main():
    #ゲームオーバーフラグ
    game_over = False
    #スコア
    score = 0
    #速さ
    speed = 25
    #隕石
    stars = []
    #キー入力
    keymap = []
    #shipの初期立置
    ship = [0,0]
    #scopeの画像
    scope_image=pygame.image.load("image/voyager/scope2.png")
    #隕石の画像
    rock_image=pygame.image.load("image/voyager/rock.png")

    #スコア用のフォント
    scorefont = pygame.font.SysFont(None,36)
    #メッセージ用フォント
    sysfont = pygame.font.SysFont(None,72)
    #ゲームオーバーメッセージ
    message_over = sysfont.render("GAME OVER!!",True,(0,255,255))
    message_rect = message_over.get_rect()
    message_rect.center = (400,400)
    #隕石をランダムに配置
    while len(stars) < 200:
        stars.append({"pos":[randint(-1600,1600),randint(-1600,1600),randint(0,4095)],"theta": randint(0,360)})

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if not event.key in keymap:
                    keymap.append(event.key)
            elif event.type == KEYUP:
                keymap.remove(event.key)
        
        if not game_over:
            score +=1
            if score % 10 == 0:
                speed +=1
            if K_LEFT in keymap:
                ship[0] -= 30
            elif K_RIGHT in keymap:
                ship[0] += 30
            elif K_UP in keymap:
                ship[1] -= 30
            elif K_DOWN in keymap:
                ship[1] += 30
            ship[0] = max(-800,min(800,ship[0]))
            ship[1] = max(-800,min(800,ship[1]))

            for star in stars:
                star["pos"][2] -= speed
                if star["pos"][2] < 64:
                    if abs(star["pos"][0]-ship[0]) < 50 and abs(star["pos"][1]-ship[1])<50:
                        game_over = True
                    star["pos"] = [randint(-1600,1600),randint(-1600,1600),4095]

        SURFACE.fill((0,0,0))
        #描面
        stars = sorted(stars,key = lambda x:x["pos"][2],reverse = True)
        for star in stars:
            zpos = star["pos"][2]
            xpos = ((star["pos"][0] - ship[0])<< 9) / zpos + 400
            ypos = ((star["pos"][1]- ship[1]) <<9) /zpos + 400
            size = (50 << 9)/zpos
            rotated = pygame.transform.rotozoom(rock_image,star["theta"],size/145)
            SURFACE.blit(rotated,(xpos,ypos))
        SURFACE.blit(scope_image,(0,0))

        if game_over:
            SURFACE.blit(message_over,message_rect)
            
        score_str  = str(score).zfill(6)
        score_image = scorefont.render(score_str,True,(0,255,0))
        SURFACE.blit(score_image,(700,50))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()