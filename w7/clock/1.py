import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        #clock.tick(60)import pygame, sys
from pygame.locals import *
from datetime import datetime

class ClockFace:        
        
        def __init__(self, imageFileName, clock_center, screen):
                self.imageFileName = imageFileName
                self.screen = screen
                self.faceSurface = pygame.image.load(imageFileName).convert()
                self.clock_center = clock_center

class ClockHand:
        
        def __init__(self, imageFileName, rotationAngle, subRotationAngle, clockFace):
                self.imageFileName = imageFileName
                self.subRotationAngle = subRotationAngle
                self.rotationAngle = rotationAngle
                self.clockFace = clockFace
                self.screen = screen
                self.handSurface = pygame.image.load(imageFileName).convert_alpha()

def rotateHand(theHand, timeUnits, subUnits):
        rotAngle = int(theHand.rotationAngle * timeUnits) + subUnits + 90
        curHand = pygame.transform.rotate(theHand.handSurface, rotAngle)
        x = theHand.clockFace.clock_center - curHand.get_width()/2
        y = theHand.clockFace.clock_center - curHand.get_height()/2
        theHand.clockFace.screen.blit(curHand, (x,y))


           
clockFaceFile = "clock.png"
handsSecondsFile = "s.png"
handsMinutesFile = "m.png"

pygame.init()   
pygame.font.init()
        
dim_clock_x, dim_clock_y = 800, 800
clock_center =  dim_clock_x/2

screen = pygame.display.set_mode((dim_clock_x, dim_clock_y), 0, 32)
clock = pygame.time.Clock()
clockFace  = ClockFace(clockFaceFile, clock_center, screen)
        

        
secondHand = ClockHand(handsSecondsFile, - 6,  0, clockFace)
minuteHand = ClockHand(handsMinutesFile, - 6, 10, clockFace)
                
        
now = datetime.now()
while True:
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        #sys.exit()
                

                        
                later = datetime.now()
                difference = (later - now).total_seconds()
                if (difference > 0):
                        now = later
                        second = now.second
                        screen.blit(clockFace.faceSurface, (0,0))
                        rotateHand(minuteHand, now.minute, -(now.second//minuteHand.subRotationAngle))
                        rotateHand(secondHand, now.second, 0)
                        pygame.time.set_timer(1, 100)
                        pygame.display.update()