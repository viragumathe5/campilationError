import pygame
import random
import time



pygame.init()

display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)

naruto_width = 73


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Naruto Jump")
clock = pygame.time.Clock()

naruto = pygame.image.load("naruto1.png")


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])





def naruto1(x, y):
    gameDisplay.blit(naruto, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameLoop()

def crash():
    message_display("Crashed") 


def colision():
       message_display("Collided")



def gameLoop():


    x = (display_width * 0.30)
    y = (display_height * 0.45)
    x_change = 0
    y_change = 0

    thing_starty = (display_height * 0.60)
    thing_startx = display_width 
    thing_speed = 10
    thing_width = 50
    thing_height = 100



    gameQuit = False

    while not gameQuit:


        
        
        for i in pygame.event.get():
            if i.type == pygame.quit:
                gameQuit = True

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    y_change = -130
                    
                    
                
            if i.type == pygame.KEYUP:
                if i.key == pygame.K_UP:
                    y_change = +130
                
                

            """
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    x_change = -5
                elif i.key == pygame.K_RIGHT:
                    x_change = +5

            if i.type == pygame.KEYUP:
                if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                    x_change = 0
            """
            print(i)




            x += x_change 
            y += y_change  
            y_change = 0

        
        gameDisplay.fill(white)


        #things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_startx -= thing_speed

        naruto1(x, y)

        if x > display_width - naruto_width or x < 0: 
            crash()
        
        if thing_startx < 0:
            thing_startx = 0 + display_width
            thing_width = random.randrange(10, 50)



        if thing_startx < x:
            if not thing_starty/2 < y and thing_startx == x : #+ thing_height: 
                colision()



        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
