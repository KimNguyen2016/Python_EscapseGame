import pygame
import time
import random
pygame.init()

# --------------------------------------------- #
display_width = 800
display_height = 600

# --------------------------------------------- #
background_color = (253,176,219)
black = (0,0,0)
white = (255, 255, 255)

yellow = (255,255,0)
light_yellow = (255,255,102)

block_color = (91,192,222)
intro_color = (255,204,92)
# --------------------------------------------- #

rabit_width = 85
pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(' Escapse ')
clock = pygame.time.Clock()
carImg = pygame.image.load('bunny_icon.jpg')

# --------------------------------------------- #

def things_dodged(count):
  font= pygame.font.SysFont(None, 25)
  text = font.render("Score: " + str(count), True, black)
  gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
  pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x,y):
  gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

def message_display(text):
  msgText = pygame.font.Font('freesansbold.ttf', 80)  
  TextSurf, TextRect = text_objects("Caught it", msgText)
  TextRect.center = ((display_width/2), (display_height/2))
  gameDisplay.blit(TextSurf, TextRect)
  pygame.display.update()
  
  time.sleep(2)
  game_loop()
  
# Crash function    
def crash():
  gameDisplay.fill(background_color)
  msgText = pygame.font.Font('freesansbold.ttf', 80)
  TextSurf, TextRect = text_objects("Caught it", msgText)
  TextRect.center = ((display_width/2), (display_height/2))
  gameDisplay.blit(TextSurf, TextRect)  
	
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
								
                
    button("Play Again", 100, 500, 150, 50, yellow, light_yellow, game_loop)
    button("EXIT", 600, 500, 150, 50, yellow, light_yellow, quitGame)
    pygame.display.update()
    clock.tick(15)	

# Button function   
def button(msg,x,y,w,h,ic,ac, action=None): 
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
	
  if x + w > mouse[0] > x and y + h > mouse[1] > y:               
    pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
    if click[0] == 1 and action !=None:
      action()
  else:
    pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
  smallText = pygame.font.Font('freesansbold.ttf', 20)  
  TextSurf, TextRect = text_objects(msg, smallText)
  TextRect.center = ((x + (w/2)), (y + (h/2)))              
  gameDisplay.blit(TextSurf, TextRect)                                   
 
 
# Quit game function
def quitGame():
	pygame.quit()
	quit()

# unpause function
def unpause():
	global pause
	pause = False

# pause function
def paused():
    msgText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects("Paused", msgText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
		
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
								
        gameDisplay.fill(intro_color)        
				
        button("Continue", 100, 500, 100, 50, yellow, light_yellow, game_loop)
        button("EXIT", 600, 500, 100, 50, yellow, light_yellow, quitGame)
        pygame.display.update()
        clock.tick(15)	
				
				
# Game_Intro function  
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
								
        gameDisplay.fill(intro_color)
        msgText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Escapse", msgText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
				
        button("PLAY", 100, 500, 100, 50, yellow, light_yellow, game_loop)
        button("EXIT", 600, 500, 100, 50, yellow, light_yellow, quitGame)
        pygame.display.update()
        clock.tick(15)
        
	

# --------------------------------------------------------------------- #   
# Game loop function #
def game_loop():
  
  x = (display_width * 0.45)
  y = (display_height * 0.77)  
  x_change = 0  
	
  thing_startx = random.randrange(0, display_width)
  thing_starty = -600
  thing_speed = 4
  thing_width = 100
  thing_height = 100
  
  thingcount = 1
  dodged = 0
  gameExit = False
  
  while not gameExit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:        
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x_change = -5
        if event.key == pygame.K_RIGHT:
          x_change = 5
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          x_change = 0
        if event.key == pygame.K_p:
          pause = True
          paused()

    x += x_change
    gameDisplay.fill(background_color)
    
    things(thing_startx, thing_starty, thing_width, thing_height, block_color)
    thing_starty += thing_speed   
    car(x,y)
    things_dodged(dodged)
    
    if  x > display_width - rabit_width or x < 0:      
      crash()
      
    if thing_starty > display_height:
      thing_starty = 0 - thing_height
      thing_startx = random.randrange(0, display_width)
      dodged += 1
      thing_speed += 1
          
      #make block bigger      
      thing_width += dodged * 1.2 
      
    if y < thing_starty + thing_height:
      #crash()    
      if x > thing_startx and x < thing_startx + thing_width or x + rabit_width > thing_startx and x + rabit_width < thing_startx + thing_width:                
        crash()           
    pygame.display.update()
    clock.tick(60)

#------------------------------------ #
game_intro()
game_loop()   
pygame.quit()
quit()
  
