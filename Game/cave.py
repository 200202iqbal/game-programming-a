import pygame
import sys
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
from random import randint

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
pygame.key.set_repeat(5, 5)

def main():
    #壁の数
    walls = 80
    #shipの初期位置
    ship_y = 250
    #加速度
    velocity = 0
    #スコア
    score = 0
    #壁の角度
    slope = randint(1, 6)
    #フォントの設定
    sysfont = pygame.font.SysFont(None, 36)
    #shipの画像読み込み
    ship_image = pygame.image.load("pygame_img/ship.png")
    #爆発の画像読み込み
    bang_image = pygame.image.load("pygame_img/bang.png")
    #洞窟のリスト
    holes = []
    #洞窟のリストの生成
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    #ゲームオーバーフラグ
    game_over = False

    while True:
        #スペースキー押されていない
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #イベントがキーダウンだったら
            elif event.type == KEYDOWN:
                #押されたキーがスペースだったら
                if event.key == K_SPACE:
                    #スペースキー押された
                    is_space_down = True

        #ゲームオーバーでなければ
        if not game_over:
            #スコアをアップ
            score +=10
            #加速度の設定
            velocity += -3 if is_space_down else 3
            #shipの位置移動
            ship_y += velocity
            edge = holes[-1].copy()
            test = edge.move(0,slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1,6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0,-20)
            edge.move_ip(10,slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10,0) for x in holes]
            if holes[0].top > ship_y or holes[0].bottom < ship_y +80:
                #ゲームオーバー
                game_over= True,

        SURFACE.fill((0, 255, 0))
        for hole in holes:
            pygame.draw.rect(SURFACE,(0,0,0),hole)
        #shipの表示
        SURFACE.blit(ship_image,(0,ship_y))
        #スコア表示
        score_image = sysfont.render("score is {}".format(score),True,(0,0,255))
        SURFACE.blit(score_image,(600,20))
        #ゲームオーバーなら
        if game_over:
            SURFACE.blit(bang_image,(0,ship_y-40))
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()