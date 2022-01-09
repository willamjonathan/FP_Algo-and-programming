import pygame
#---------------------------------------------------------------------------------------
from defaultgame import main
from hard import mainhard
from medium import mainmedium
#--------------------------------------------------------------------------------------
from screen import myFPS
from screen import screen_size
from screen import MyColor
from screen import myFont

pygame.init()
pygame.font.init()

#calling function
font1 = myFont('Arial')
font2 = myFont( )
ss = screen_size(800,600)
Fps = myFPS(60)
cl = MyColor()

myscreen = pygame.display.set_mode((ss.getWidth(),ss.getHeight()))
bg = pygame.image.load("menubg.jpg")
myscreen.blit(bg,(0,0))
clock = pygame.time.Clock()

def mainpage():
    #title text
    titlefont = pygame.font.SysFont(font1.getMyFont(),60)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("UFO WORLD DOMINATION", True, (0,0,0))
        myscreen.blit(TTL_text, (100,170))

    #my button
    button = 0
    playFont = pygame.font.SysFont(font2.getMyFont(),24)
    def myButton(myscreen):
        if button == 0:  
            text = playFont.render("'Choose your enemy'", 1, (cl.getColor()),(122,122,122))
            myscreen.blit(text, (210, 280))
            text1 = playFont.render("'instructions of how to play'",1, (cl.getColor()),(122,122,122))
            myscreen.blit(text1, (350,400))
            text2 = playFont.render("arrow left and right keystroke to move  in X direction",1, (cl.getColor()),(122,122,122))
            myscreen.blit(text2, (370,420))
            text3 = playFont.render("use space to shoot",1, (cl.getColor()),(122,122,122))
            myscreen.blit(text3, (370,440))
            easy = playFont.render("SKULL(use arrow left keystroke)", 1, (255,0,0))
            myscreen.blit(easy, (270, 310))
            medium = playFont.render("TAKO (use arrow down keystroke)", 1, (255,0,255))
            myscreen.blit(medium, (270, 330))
            hard = playFont.render("MONSTER(use arrow right keystroke)", 1, (0,255,0))
            myscreen.blit(hard, (270, 350))
        elif button == 1:  #page1
            text = playFont.render(main(),1,(0,0,0))
        elif button == 2: #page2
            text = playFont.render(mainmedium(),1,(0,0,0)) 
        elif button == 3: #page3
            text = playFont.render(mainhard(),1,(0,0,0))
    running = True
    while running:
        clock.tick(Fps.getFPS())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button = 1#easy
                if event.key == pygame.K_DOWN:
                    button = 2#medium
                elif event.key == pygame.K_RIGHT:
                    button = 3#hard
            else:
                button = 0

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()

    pygame.quit()

mainpage()