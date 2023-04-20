import sys 
import pygame as pg

#Default color
R = 255
G = 0
B = 0

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(R,G,B),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if(mouseX >= self.x and mouseY >= self.y and mouseX <=self.x + self.w and mouseY <= self.y + self.h):
            return True
        else:
            return False
        
    def isMouseClick(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn() and btn.isMouseClick():
        R = 160
        G = 32
        B = 240
    elif btn.isMouseOn():
        R = 128
        G = 128
        B = 128
    else:
        R = 255
        G = 0
        B = 0

    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    