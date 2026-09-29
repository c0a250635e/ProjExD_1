import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False) #lec8
    kt_img = pg.image.load("fig/3.png") #lec3
    kt_img = pg.transform.flip(kt_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #lec9
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0]) #lec7
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(kt_img, [300, 200]) #lec4
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()