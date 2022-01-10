#imports---------------------------------------------------------------------------------------------
#from screenpy--------------------------------------
from screen import MyColor #importing from another file that class to get the screen fill color
from screen import myFPS # importing from screen file
from screen import screen_size
from screen import p_position
from screen import myFont 
#from mainmenu import mainpage
#---------------------------------------------------
import pygame
import random#importing random for random position
import math#for math equation
from pygame import mixer 
#------------------------------------------------------------------------------------------------------
pygame.init()
pygame.font.init()

#screen size
SS = screen_size(800, 600) #setting the width and height
myscreen = pygame.display.set_mode((SS.getWidth(),SS.getHeight()))#screen setting display

#game title and icon
pygame.display.set_caption("UFO WORLD DOMINATION")#title
logo = pygame.image.load("game3_icon.png") #icon
pygame.display.set_icon(logo)#icon
#calling functions-------------------------------------------------------------------------------------
cs = MyColor() #calling the function from MyColor class
FPS = myFPS() #calling the funciton from myFPS class
plyr1 = p_position(370,450)
mF = myFont()
#background---------------------------------------------------------------------------------------------
#background image
background =  pygame.image.load("background2.jpg")

#background sound
mixer.music.load('background2.wav')
mixer.music.play(-1)#looping the sound

#background function
def display_bg():
    myscreen.fill(cs.getColor())#importing from other file that have class <line2>
    myscreen.blit(background,(0,0))
#-------------------------------------------------------------------------------------------------------
#The ufo image
ufoImg = pygame.image.load("ufo.png")
#ufo function
def ufo(x,y):
    myscreen.blit(ufoImg, (x,y))

#The star image-----------------------------------------------------------------------------------------
starImg = pygame.image.load("star1.png")
star_condition = "loaded"
#showing the star on screen
def shoot_star(x,y):
    myscreen.blit(starImg,(x + 15.5,y + 0.8))#to make it appear on the middle of the UFO
#-------------------------------------------------------------------------------------------------------
#crash between skull and star
def crashing(skullX,skullY,starX,starY):
    #calculating distance between skull and star
    d = math.sqrt((math.pow(skullX - starX, 2))+ (math.pow(skullY - starY, 2)))
    if d < 27:
        return True
    else:
        return False
        

#main funciton ------------------------------------------------------------------------------------------
def main():#looping for the screen to be displayed continously
#if this function doesn't exist, the screen will be only displayed by a few second
#ufoX position in the screen; its not inside for bcs if not it cant change position if key is up

    #My Ufo info---------------------------------------------------------
    ufoX =plyr1.getUfoX()
    ufoY =plyr1.getUfoY()
    ufoX_movement = 0.5
    ufoY_movement = 0
    #My Skull---------------------------------------------------------------
    #My Skull info
    #creating multiple enemies by using list and for loop
    skullImg=[]
    skullX=[]
    skullY=[]
    skullX_movement= []
    skullY_movement= []

    NOE = 6 #number of enemies 
    #adding skull to the list 
    for z in range(NOE):
        skullImg.append(pygame.image.load("skull.png"))
        skullY.append(random.randint(50, 150))
        skullX.append(random.randint(0,735))
        skullX_movement.append(3)
        skullY_movement.append(40)

    def skull(x,y,z):
        myscreen.blit(skullImg[z], (x,y))
    #----------------------------------------------------------------------
    
    #My Star info
    #loaded - star can't be seen on screen
    #shoot - the star is currently moving
    star_condition ="loaded"#star state right now when nothing is pressed
    starX = 0
    starY = 480
    starX_movement = 0
    starY_movement = 10

    #My Score info---------------------------------------------------------
    #score
    myscore = 0
    textX = 10
    textY = 10
    font = pygame.font.Font(mF.getMyFont(),32)#('font',size)
    def displaypoint(x,y):    
        score = font.render("Score :" + str(myscore),True, (cs.getColor()))
        myscreen.blit(score, (x,y))
    #----------------------------------------------------------------------
    #game over txt
    the_font = pygame.font.Font(mF.getMyFont(),64)
    clickfont = pygame.font.Font(mF.getMyFont(),16)
    def lose_text():
        GO_text = the_font.render("GAME OVER", True, (cs.getColor()))
        myscreen.blit(GO_text, (200,250))
        C_text = clickfont.render("click anywhere on the screen",True, (cs.getColor()))
        myscreen.blit(C_text, ( 280,380))

    #try again-------------------------------------------------------------
    button = 0
    TA_font = pygame.font.Font(mF.getMyFont(),32)
    def tryagain_text():
        if button == 0:
            TA_text = TA_font.render("TRY AGAIN?",True, (cs.getColor()))
            myscreen.blit(TA_text, (300,335))
        elif button == 1:
            text = TA_font.render(main(),1,(0,0,0))

    clock = pygame.time.Clock()
    running = True#the loop
    while running:
        display_bg()#calling the display_color function 
        clock.tick(FPS.getFPS())#controlling the speed of the while loop in any computer (never go more than 60 fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quiting the pygame 
                running = False #by pressing quit, it will stop running

        #if keystroke in keyboard is pressed, then :------------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if star_condition is "loaded":#so if it is still firing it can't shoot
                    #assigning starX so it comes out of the UFO current on the firing position
                        starX = ufoX 
                        star_Sound = mixer.Sound('shoot.wav')
                        star_Sound.play()
                        shoot_star(starX, starY)#calling shoot star function(showing the image)
                        star_condition = "shoot"#assigning the star_condition to loaded
                if event.key == pygame.K_LEFT:
                    ufoX_movement = -5.5
                if event.key == pygame.K_RIGHT:
                    ufoX_movement = +5.5
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = 1
        #--------------------------------------------------------------------------------------------------
    #movement---------------------------------------------------------------------------------------------
    #ufo movement  
    #basically it is the boundaries so it doesnt go out of the screen
        ufoX += ufoX_movement
        if ufoX <= 0:
            ufoX = 0
        elif ufoX >= 734:
            ufoX = 734
    #skull movement
        for z in range(NOE):
            #game over 
            if skullY[z]>365:
                for d in range(NOE):
                    skullY[d]=2000
                lose_text()#calling game over text
                tryagain_text()
                break
    #skull boundaries
            skullX[z] += skullX_movement[z]#to let our program now which skullmovement are we talking about
            if skullX[z] <= 0:
                skullX_movement[z] = 3
                skullY[z] += skullY_movement[z]
            elif skullX[z] >= 734:
                skullX_movement[z] = -3
                skullY[z] += skullY_movement[z]
        #crash
            crash = crashing(skullX[z],skullY[z],starX,starY)
            if crash : #if crash happens 
                crash_Sound = mixer.Sound('crash.wav')
                crash_Sound.play()
                starY = 480
                star_condition = "loaded"
                myscore +=1 #score will increase
    #if skull is hit by star, the skull will respawn
                skullY[z] = random.randint(50, 150)
                skullX[z] = random.randint(0, 730)
            skull(skullX[z],skullY[z],z)#calling the skull function

    #star movement
        #if the star has reached the top, the state will be loaded again which mean it can shoot again
        if starY <=0 :
            starY = 480
            star_condition = "loaded"
        #starY movement
        if star_condition is "shoot":
            shoot_star(starX, starY)
            starY -= starY_movement #goes to the top of the screen
    #---------------------------------------------------------------------------------------------------
        
        ufo(ufoX,ufoY)#calling the ufo function
        displaypoint(textX,textY)#calling the displaypoint funciton
        pygame.display.update()#updating the display
    pygame.quit()
#--------------------------------------------------------------------------------------------------------
