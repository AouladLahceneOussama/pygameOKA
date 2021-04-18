from mission import Mission
import pygame
import math

pygame.init()
pygame.font.init()

# class Game
class Game(Mission):
    def __init__(self):
        super().__init__()
        self.isMenu = False
        
    def showMenu(self, screen):
        self.title = pygame.font.SysFont("Arial",48,True)
        self.text = self.title.render("Missions", True, (255,255,255))
        screen.blit(self.text, (440,150))

        self.subTitle = pygame.font.SysFont("Arial",24,True)
        self.text = self.subTitle.render("[ Click to choose a mission ]", True, (174,179,188))
        screen.blit(self.text, (370,220))

        #add menu items
        self.item1 = pygame.image.load("assets/images/mission1.png")
        self.item1 = pygame.transform.scale(self.item1,(200,200))
        screen.blit(self.item1,(150,300))
        self.itemRect1 = self.item1.get_rect()
        self.itemRect1.x = 150
        self.itemRect1.y = 300

        self.item2 = pygame.image.load("assets/images/mission2.png")
        self.item2 = pygame.transform.scale(self.item2,(200,200))
        screen.blit(self.item2,(450,300))
        self.itemRect2 = self.item2.get_rect()
        self.itemRect2.x = 450
        self.itemRect2.y = 300

        self.item3 = pygame.image.load("assets/images/mission3.png")
        self.item3 = pygame.transform.scale(self.item3,(200,200))
        screen.blit(self.item3,(750,300))
        self.itemRect3 = self.item3.get_rect()
        self.itemRect3.x = 750
        self.itemRect3.y =300
    
                
