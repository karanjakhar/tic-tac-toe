import pygame
from time import sleep
import random
x=150
y=300
pygame.init()
gameDisplay=pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-Tac-Toe')
clock=pygame.time.Clock()
white=(255,255,100)
black=(0,0,0)

mess=0
cor=[]
o_co=[]
box1=box2=box3=box4=box5=box6=box7=box8=box9=True

centre_co=[[200,250],[300,250],[400,250],[200,350],[300,350],[400,350],[200,450],[300,450],[400,450]]
crashed=False
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,cor):
    for i in cor:

            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (i)
            gameDisplay.blit(TextSurf, TextRect)
while not crashed:

    gameDisplay.fill(white)
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True
        print(event)
        if event.type==pygame.MOUSEBUTTONDOWN:
            click_x,click_y=pygame.mouse.get_pos()
            if click_x<=250 and click_x>=150 and click_y<=300 and click_y>=200:
                if box1:
                    mess+=2
                    cor.append([200,250])
                    centre_co.remove([200,250])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box1=False
                
            elif click_x<=350 and click_x>=250 and click_y<=300 and click_y>=200:
                if box2:
                    mess+=2
                    cor.append([300,250])    
                    centre_co.remove([300,250])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box2=False
            elif click_x<=450 and click_x>=350 and click_y<=300 and click_y>=200:
                if box3:
                    mess+=2
                    cor.append([400,250])    
                    centre_co.remove([400,250])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box3=False
            elif click_x<=250 and click_x>=150 and click_y<=400 and click_y>=300:
                if box4:
                    mess+=2
                    cor.append([200,350])    
                    centre_co.remove([200,350])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box4=False
            elif click_x<=350 and click_x>=250 and click_y<=400 and click_y>=300:
                if box5:
                    mess+=2
                    cor.append([300,350])    
                    centre_co.remove([300,350])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box5=False
            elif click_x<=450 and click_x>=350 and click_y<=400 and click_y>=300:
                if box6:
                    mess+=2
                    cor.append([400,350])    
                    centre_co.remove([400,350])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box6=False
            elif click_x<=250 and click_x>=150 and click_y<=500 and click_y>=400:
                if box7:
                    mess+=2
                    cor.append([200,450])    
                    centre_co.remove([200,450])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    
                    box7=False
            elif click_x<=350 and click_x>=250 and click_y<=500 and click_y>=400:
                if box8:
                    mess+=2
                    cor.append([300,450])    
                    centre_co.remove([300,450])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    box8=False
            elif click_x<=450 and click_x>=350 and click_y<=500 and click_y>=400:
                if box9:
                    mess+=2
                    cor.append([400,450])    
                    centre_co.remove([400,450])
                    if centre_co:
                      o_co.append(random.choice(centre_co))
                    
                    box9=False
            print(x," ",y)
    pygame.draw.line(gameDisplay,2,[x,y],[x+300,y],4)
    pygame.draw.line(gameDisplay,4,[x+100,y-100],[x+100,y+200],4)
    pygame.draw.line(gameDisplay,2,[x+200,y-100],[x+200,y+200],4)
    pygame.draw.line(gameDisplay,2,[x,y+100],[x+300,y+100],4)
    if mess:
        
            message_display("X",cor)
            message_display("O",o_co)
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()

        
