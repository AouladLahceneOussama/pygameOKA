import pygame
import random

class Mission():
    def __init__(self):
        self.mission = 0
        self.missionStart = False 
        #answers first mission
        self.planetAnswer = {1:53,
                            2:49,
                            3:54,
                            4:55,
                            5:57,
                            6:56,
                            7:51,
                            8:52,
                            9:50
                            }
        #answers second mission
        self.planet2Answer = {1:54,
                            2:56,
                            3:50,
                            4:49,
                            5:55,
                            6:57,
                            7:52,
                            8:51,
                            9:53
                            }
        #answers second mission
        self.planet3Answer = {1:49,
                            2:50,
                            3:50,
                            4:49
                            }
        self.planetQs = 1

        #listeImages
        self.listePlanets=[
            pygame.image.load("assets/images/planets/1.png"),
            pygame.image.load("assets/images/planets/2.png"),
            pygame.image.load("assets/images/planets/3.png"),
            pygame.image.load("assets/images/planets/4.png"),
            pygame.image.load("assets/images/planets/5.png"),
            pygame.image.load("assets/images/planets/6.png"),
            pygame.image.load("assets/images/planets/7.png"),
            pygame.image.load("assets/images/planets/8.png"),
            pygame.image.load("assets/images/planets/9.png")
        ]

    #sonares effects
    def soundEffect(self,sound):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(0)

  
    def showMission(self,screen):
        if self.mission == 1:
            self.planetsName(screen,self.planetQs)

        elif self.mission == 2:
            self.planetPlace(screen,self.planetQs)

        elif self.mission == 3:
            self.moon(screen,self.planetQs)
        
    #mission 1 methods  
    def planetsName(self,screen,question):
        self.planetsDes = [
            ['I am the red planet. I am smaller than Earth and Venus. ','I have an atmosphere of mostly carbon dioxide.',' My surface, peppered with vast volcanoes. Who I am ?'],
            ['I am the hottest and the second fastest planet in the system.','Most of my atmosphere made of dioxide of carbon.','My day is longer than my year.Who I am ?'],
            ['I radiate more internal heat, but not as much as Jupiter or Saturn.','I am accompanied in my orbit by several minor planets.','Who I am ?'],
            ['I am the smallest planet in the entire system ','I have no atmosphere.The astronomy scientists had already ','removed me from the planets list. Who I am ?'],
            ['I am the largest and densest of the inner planets,','the only one known to have current geological activity,','and the only place where life is known to exist. Who I am ?'],
            ['I almost have no atmosphere My year takes 88 of your days','And my day takes 59. I am very cold at night','and very hot on the day.Who I am ?'],
            ['I am distinguished by my extensive ring system.','I am the only planet of the Solar System that is ','less dense than water.Who I am ?'],
            ['I am the lightest of the outer planets.','I have a much colder core than the other giant ','planets and radiates very little heat into space. Who I am ?'],
            ['I am the biggest planet in the system.','I am made up of only gazes My year is 29 earth years.','My day take only 10 hours Who I am ?']
            ]

        self.desFont = pygame.font.SysFont("Arial",20,True)

        for i in range(1,11):
            if question == i and i <10:
                self.planetImage = pygame.image.load("assets/images/planets/"+ str(i) +".png")
                self.planetImage = pygame.transform.rotate(self.planetImage, 250)
                self.planetNamesScreen(screen,self.planetImage)            
                for j in range(1,4):
                    self.Des = self.desFont.render(self.planetsDes[i-1][j-1], True, (255,252,0))
                    screen.blit(self.Des, (100,400 + j*30))

            if question == 10:
                screen.blit(pygame.image.load("assets/images/end.png"),(80,80))
                #self.soundEffect("assets/sounds/win.mp3")
                
        
    def planetNamesScreen(self,screen,image):
        screen.blit(image,(180,200))
        self.title = pygame.font.SysFont("Arial",48,True)
        self.text = self.title.render("Let's Discover our Galaxy", True, (255,255,255))
        screen.blit(self.text,(200,50))

        self.subTitle = pygame.font.SysFont("Arial",30,True)
        self.planets = ['[1] Venus','[2] Jupiter','[3] Saturne','[4] Uranus','[5] Mars','[6] Neptune','[7] Pluto','[8] Mercury','[9] Earth']
        
        for i in range(1,10):        
            self.text = self.subTitle.render(self.planets[i-1], True, (255,252,0))
            screen.blit(self.text, (850,200 + i*35))

        self.text = self.subTitle.render("[ Press number to choose the right planet ]", True, (174,179,188))
        screen.blit(self.text,(200,650))


    def getKeyPressed(self,screen,keyPressed):
        self.keys = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_SPACE]
        for k in self.keys:
            if keyPressed == k:  
                if self.planetQs in self.planetAnswer and self.planetAnswer[self.planetQs] == k and self.mission == 1:
                    self.planetQs += 1
                    self.planetsName(screen,self.planetQs)
                        
                elif self.planetQs in self.planet2Answer and self.planet2Answer[self.planetQs] == k and self.mission == 2:
                    self.planetQs += 1
                    self.planetPlace(screen,self.planetQs)
                        
                elif self.planetQs in self.planet3Answer and self.planet3Answer[self.planetQs] == k and self.mission == 3:
                    self.planetQs += 1
                    self.moon(screen,self.planetQs)
                    
                elif k == 32:
                    self.planetQs = 1
                    self.missionStart = False


    #mission 2 methods
    def planetPlace(self,screen,question):
        for i in range(1,11):
            if question == i and i < 10:
                self.planetImage = pygame.image.load("assets/images/planets/"+ str(i) +".png")
                self.planetPlaceScreen(screen,self.planetImage)  
                self.drawPlanets(screen,question)

            elif question == 10:
                screen.blit(pygame.image.load("assets/images/end.png"),(80,80))
                #self.soundEffect("assets/sounds/win.mp3")
                
                         
    def planetPlaceScreen(self,screen,image):
        screen.blit(image,(100,400))
        self.solarSys = pygame.image.load("assets/images/Sorbite.png")
        screen.blit(self.solarSys, (180,10))

        for i in range(1,10):
            self.text = self.subTitle.render("["+str(i)+"]", True, (174,179,188))
            screen.blit(self.text,(140 +i*73 ,10))

        self.text = self.subTitle.render("[ Press number that match with the right orbite ]", True, (174,179,188))
        screen.blit(self.text,(200,650))

    def drawPlanets(self,screen,imageNumber):
        for i in reversed(range(0,imageNumber-1)):
            answer = self.planet2Answer[i+1] - 48
            self.listePlanets[i] = pygame.transform.scale(self.listePlanets[i],(80,80))
            if answer%2 == 0:
                screen.blit(self.listePlanets[i],(110 + answer*81,100 +((-1)**answer*50)))
            else:
                screen.blit(self.listePlanets[i],(110 + answer*78,100 +((-1)**answer*50)))


    #mission 3
    def moon(self,screen,question):
        self.text = self.subTitle.render("[ Press the right number (1,2,3) ]", True, (174,179,188))

        for i in range(1,6):    
            if question == i and i < 5 :
                    self.planetImage = pygame.image.load("assets/images/questions/q"+ str(i) +".png")
                    screen.blit(self.planetImage,(100,80))
                    screen.blit(self.text,(300,650))
            
            if question == 5:
                screen.blit(pygame.image.load("assets/images/end.png"),(80,80))
                #self.soundEffect("assets/sounds/win.mp3")



 