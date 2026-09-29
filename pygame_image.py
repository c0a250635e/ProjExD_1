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
    kt_rct = kt_img.get_rect() #lec10-1
    kt_rct.center = 300, 200 #lec10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #lec10-3

        tate = 0
        yoko = -1
        if key_lst[pg.K_UP]:
            tate = -1
        if key_lst[pg.K_DOWN]:
            tate = +1
        if key_lst[pg.K_LEFT]:
            yoko = -1
        if key_lst[pg.K_RIGHT]:
            yoko = +1
        
        kt_rct.move_ip(yoko, tate)

        x = tmr%3200 #lec9
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0]) #lec7
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(kt_img, kt_rct) #lec4
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()