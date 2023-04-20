import sys
import pygame as pg

r = 153
g = 255
b = 51

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0): #สร้างตัวแปรใน rec
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen): # ฟังก์ชั่นที่ใช้ข้างนอก argument self , screen
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if (mouseX >= self.x and mouseY >= self.y and mouseX <= self.x + self.w and mouseY <= self.y + self.h):
            return True
        else:
            return False
    def MousePress(self) :
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False

class InputBox:

    def __init__(self, x, y, w, h, alpha ,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color) #
        self.active = False 
        self.alpha = alpha #คนละตัว ขวารับจากนอก class

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active 
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.alpha is True :
                        self.text += event.unicode #unicode ตัวอักษรที่เขียนเข้าไปจะมี unicode ของมันเอง
                    else :
                        if chr(event.key).isnumeric():
                            self.text += event.unicode #unicode ตัวอักษรที่เขียนเข้าไปจะมี unicode ของมันเอง
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color) # render font ทำให้ออกมาเป็นตัวอักษรบน screen
        
    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width #ความกว้างช่องในตอนแรก ถ้าตัวอักษรเกิน box ที่ตั้งไว้ มันจะเพิ่มขึ้นเรื่อยๆ ขยายขนาด

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5)) #textbox ที่ใส่เข้าไป blit display text box ลงไปที่ screen , +5 คือ offset เฉยๆ
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2) # 2 คือขอบความหนา



pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('orange') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('firebrick')     # ^^^
FONT = pg.font.Font(None, 28)

font = pg.font.Font('freesansbold.ttf', 28) # font and fontsize
text = font.render('Firstname', True, "sea green") # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (150, 50)
text1 = font.render('Lastname', True, "sea green") # (text,is smooth?,letter color,background color)
textRect1 = text.get_rect() # text size
textRect1.center = (450, 50)
text2 = font.render('Age', True, "sea green") # (text,is smooth?,letter color,background color)
textRect2 = text.get_rect() # text size
textRect2.center = (150, 153)
text6 = font.render('University', True, "sea green") # (text,is smooth?,letter color,background color)
textRect6 = text.get_rect() # text size
textRect6.center = (450, 153)
text3 = font.render('submit', True, "black") # (text,is smooth?,letter color,background color)
textRect3 = text.get_rect() # text size
textRect3.center = (165, 275)
# text new
text4 = font.render('', True, "chartreuse") # (text,is smooth?,letter color,background color)
textRect4 = text.get_rect() # text size
textRect4.center = (400, 79)
text5 = font.render('', True, "chartreuse") # (text,is smooth?,letter color,background color)
textRect5 = text.get_rect() # text size
textRect5.center = (400, 182)


input_box1 = InputBox(80, 65, 140, 32, True) # สร้าง InputBox1
input_box2 = InputBox(378, 65, 140, 32, True) # สร้าง InputBox2
input_box3 = InputBox(80, 170, 140, 32, False) # สร้าง InputBox3
input_box4 = InputBox(378, 170, 140, 32, True) # สร้าง InputBox3
btn1 = Button(80,260,140,32)
input_boxes = [input_box1, input_box2,input_box3,input_box4] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

while run:
    screen.fill((255, 255, 255))
    screen.blit(text,textRect)
    screen.blit(text1,textRect1)
    screen.blit(text2,textRect2)
    
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    if btn1.isMouseOn() and btn1.MousePress():
        text4 = font.render('Hello '+ input_box1.text + "  " + input_box2.text + "!" , True, "black") # (text,is smooth?,letter color,background color)
        text5 = font.render("You are " + input_box3.text + " years old."  , True, "black")
    
    screen.blit(text6,textRect6)
    screen.blit(text5,textRect5)
    screen.blit(text4,textRect4)
    btn1.draw(screen)
    screen.blit(text3,textRect3)
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()