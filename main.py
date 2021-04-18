from game import Game
import pygame
import math

pygame.init()
pygame.font.init()

#global variables for screen
pygame.display.set_caption("Planet Discovery") #title in heade of application or game
screen = pygame.display.set_mode((1080,720)) #set the size of our game

#import images background
back = pygame.image.load("assets/images/back.jpg") #add the path of image
back = pygame.transform.scale(back,(1080,720))

#import playBtn
playBtn = pygame.image.load("assets/images/playBtn.png") #add the path of image
playBtn = pygame.transform.scale(playBtn,(200,200))

playBtnRect = playBtn.get_rect()
playBtnRect.x = 250
playBtnRect.y = 380

#import playLogo
logo=pygame.image.load("assets/images/playLogo.png")
logo=pygame.transform.scale(logo,(700,700))

game = Game()
run = True
while run:
    
    #add background
    screen.blit(back,(0,0))
    if game.missionStart:
        game.showMission(screen)
        
    else:    
        if game.isMenu:
            game.showMenu(screen)
        else :
            screen.blit(logo,(150,10))
            screen.blit(playBtn,(250,380))

    #update the screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playBtnRect.collidepoint(event.pos):
                game.isMenu = True

            elif game.isMenu:
               
                if game.itemRect1.collidepoint(event.pos):
                    game.missionStart = True
                    game.mission = 1
                    
                elif game.itemRect2.collidepoint(event.pos):
                    game.missionStart = True
                    game.mission = 2
                
                elif game.itemRect3.collidepoint(event.pos):
                    game.missionStart = True
                    game.mission = 3
            

        elif event.type == pygame.KEYDOWN:
            game.getKeyPressed(screen,event.key)
                
