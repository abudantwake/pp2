import pygame

pygame.init()
all_rects = []

NAME_TO_RGBA = pygame.color.THECOLORS
RGBA_TO_NAME = {}
for name, rgb in NAME_TO_RGBA.items():
    if rgb in RGBA_TO_NAME:
        RGBA_TO_NAME[rgb].append(name)
    else:
        RGBA_TO_NAME[rgb] = [name]

font = pygame.font.SysFont("monospace", 20)


blue = (0,0,255)

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

class Rect():
    def __init__(self,name, color, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.color = color
        all_rects.append(self)
    def Draw(self):
        pygame.draw.rect(screen, (self.color), self.rect)

class ColorPicker():
    def __init__(self):
        self.colors = RGBA_TO_NAME
        self.MakeGrid()
    def MakeGrid(self):
        x, y = 600, 200
        i = 0
        for col, name in self.colors.items():
            rect = Rect(name, col, x, y)
            x += 10
            i += 1
            if i == 25:
                i = 0
                y += 10
                x = 600

isPressed = False
prevPoint = (0, 0)
curPoint = (0, 0)

name_label = font.render("", 1, (255,255,255))
color_label = font.render("", 1, (255,255,255))


currentTool = 0
toolCount = 3
curColor=blue
def drawRectangle(surface, x,y, w, h):
    pygame.draw.rect(surface, curColor, [x, y, w, h],5)

def drawCircle(surface, x,y):
    pygame.draw.circle(surface, curColor, (x, y), 30)

def drawLine(surface, startPos, endPos):
    pygame.draw.line(surface, curColor, startPos, endPos, 2)
ColorPicker()
screen.fill((255,255,255))

while True:



    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                currentTool = (currentTool + 1) % toolCount
            if event.key == pygame.K_SPACE:
                screen.fill((255,255,255))
        if event.type == pygame.MOUSEBUTTONDOWN and mx <500:
            isPressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            prevPoint =pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEMOTION and isPressed == True and mx<500:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and mx>500:
            if event.button == 1:
                for rect in all_rects:
                    if rect.rect.collidepoint((mx,my)):
                        name_label = font.render(str(rect.name), 1, (0,0,0))
                        color_label = font.render(str(rect.color), 1, (0,0,0))
                        curColor=rect.color

    if currentTool == 0 and isPressed:
        drawLine(screen, prevPoint, curPoint)
    elif currentTool == 1 and isPressed:
        drawRectangle(screen, curPoint[0],curPoint[1],100,100)
    elif currentTool == 2 and isPressed:
        drawCircle(screen,curPoint[0],curPoint[1])


    background = pygame.Surface((500, 500))
    background.fill((255, 255, 255))
    screen.blit(background, (500, 0))
    screen.blit(name_label, (600, 50))
    screen.blit(color_label, (600, 100))
    for rect in all_rects:
        rect.Draw()

    pygame.draw.rect(screen, (0,0,0), [500, 0, 500, 500],5)





    pygame.display.flip()
