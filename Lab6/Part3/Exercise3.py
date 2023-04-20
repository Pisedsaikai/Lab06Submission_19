import sys
import pygame as pg

r = 255
g = 255
b = 255

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0): #สร้างตัวแปรใน rec
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen): # ฟังก์ชั่นที่ใช้ข้างนอก argument self , screen
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))

class InputBox:

    def __init__(self, x, y, w, h, alpha ,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.alpha = alpha

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.alpha is True:
                        # Check if shift key is pressed and allow uppercase letters
                        keys = pg.key.get_pressed()
                        if chr(event.key).isalpha() and not keys[pg.KMOD_SHIFT]:
                            self.text += event.unicode.lower()
                        else:
                            self.text += event.unicode
                    else:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if (mouseX >= self.x and mouseY >= self.y and mouseX <= self.x + self.w and mouseY <= self.y + self.h):
            return True
        else:
            return False
    def isMousePress(self) :
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

font = pg.font.SysFont(None, 28) # font and fontsize

text = font.render('Firstname',True,'dodgerblue2')
textRect = text.get_rect() # text size
textRect.center = (130,60)
text1 = font.render('Lastname',True,'dodgerblue2')
textRect1 = text.get_rect()
textRect1.center = (130,120)
text2 = font.render('Age',True,'dodgerblue2')
textRect2 = text.get_rect()
textRect2.center = (130,180)
text3 = font.render('Submit',True,'dodgerblue2')
textRect3 = text.get_rect()
textRect3.center = (130,300)

#output
textout1 = font.render('',True,'dodgerblue2')
textRect4 = text.get_rect()
textRect4.center = (400,300)
textout2 = font.render('',True,'dodgerblue2')
textRect5 = text.get_rect()
textRect5.center = (400,350)

input_data1 = InputBox(80, 70, 140, 32, True) # สร้าง InputBox1
input_data2 = InputBox(80, 130, 140, 32, True) # สร้าง InputBox2
input_data3 = InputBox(80, 195, 140, 32, False)
btn = Button(80,300,150,32)
input_data =[input_data1, input_data2, input_data3]

run = True

while run:
    screen.fill((255, 255, 255))
    screen.blit(text,textRect)
    screen.blit(text1,textRect1)
    screen.blit(text2,textRect2)
    mods = pg.key.get_mods()

    for data in input_data: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        data.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        data.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
    if btn.isMouseOn() and btn.isMousePress():
        if input_data1.text == "":
            if input_data2.text == "":
                textout1 = font.render("First and lastname is missing.",True,'red')
            else:
                textout1 = font.render("Firstname is missing.",True,'red')
                textout2 = font.render("",True,'black')
        elif input_data2.text == "":
            textout1 = font.render("Lastname is missing.",True,'red')
            textout2 = font.render("",True,'black')
        elif input_data3.text == "":
            textout1 = font.render("Age is missing.",True,'red')
            textout2 = font.render("",True, 'black')
        else:
            textout1 = font.render('Hello' + input_data1.text + "  " + input_data2.text + '!',True, 'dodgerblue2')
            textout2 = font.render('You are ' + input_data3.text + "year old.",True, 'dodgerblue2')

    screen.blit(textout1,textRect4)
    screen.blit(textout2,textRect5)
    btn.draw(screen)
    screen.blit(text3,textRect3)
        
    for event in pg.event.get():
        for box in input_data:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()