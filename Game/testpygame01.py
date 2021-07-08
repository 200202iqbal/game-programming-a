### testpygame01.py ###
### pip install pygame ###
### for upgrade :
### python.exe -m pip install --upgrade pip
import pygame
import sys
from pygame.locals import QUIT

#pygameの初期化
pygame.init()
#ウインドウオブジェクトの生成
SURFACE = pygame.display.set_mode((400,300))
#ウインドウのタイトルの設定
pygame.display.set_caption("Test Window")
#クロックオブジェクトの生成
FPSCLOCK = pygame.time.Clock()

#メイン処理の定義
def main():
    #フォントの設定
    sysfont = pygame.font.SysFont(None,36)
    #カウンタの初期化
    counter = 0
    #ずっと繰り返し
    while True:
        #ウインドウの色の設定
        SURFACE.fill((255,255,255))
        #イベントの取り出し
        for event in pygame.event.get():
            #イベントが[閉じる]だったら
            if event.type == QUIT:
                #pygame終了
                pygame.quit()
                #ウインドウを閉じる
                sys.exit()
        #カウントアップ
        counter +=1
        #表示用オブジェクト生成
        count_image = sysfont.render("count is {}".format(counter),True,(0,0,0))
        #表示
        SURFACE.blit(count_image,(50,50))
        #ウインドウ更新
        pygame.display.update()
        #ループの調整
        FPSCLOCK.tick(10)


#直接実行されたら
if __name__ == "__main__":
    main()