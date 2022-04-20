import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 800
FPS = 60
FONT = pygame.font.Font(None, 25)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')

class PAINT:
    def __init__(self):
        self.mode = 'rect'
        self.color = 'black'
        self.isdraw = False

    def draw(self):
        if self.mode == 'circle' and self.isdraw:
            pygame.draw.circle(WIN, self.color, (pos_x, pos_y), 25)
        elif self.mode == 'rect' and self.isdraw:
            pygame.draw.rect(WIN, self.color, (pos_x - 25, pos_y - 25, 50, 50))
        elif self.mode == 'er' and self.isdraw:
            pygame.draw.circle(WIN, 'white', (pos_x, pos_y), 25)

        self.panel()

    def change_mode(self, mode):
        self.mode = mode

    def panel(self):
        pygame.draw.rect(WIN, 'grey', (0, 0, WIDTH, 100))
        pygame.draw.circle(WIN, 'black', (50, 50), 20)
        pygame.draw.rect(WIN, 'black', (80, 30 , 40, 40))
        self.button('white', 130)
        txt = FONT.render('ER', 1, 'black')
        WIN.blit(txt, (132, 32))
        self.button('white', 600)
        self.button('black', 650)
        self.button('red', 700)
        self.button('green', 750)
        self.button('blue', 800)
    
    def button(self, color, x):
        pygame.draw.rect(WIN, 'black', (x, 30 , 40, 40))
        pygame.draw.rect(WIN, color, (x+2, 32 , 36, 36))

WIN.fill('white')

paint = PAINT()
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    pos_x, pos_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 30 <= pos_x <= 70 and 30 <= pos_y <= 70:
                paint.change_mode('circle')
            elif 80 <= pos_x <= 120 and 30 <= pos_y <= 70:
                paint.change_mode('rect')
            elif 130 <= pos_x <= 170 and 30 <= pos_y <= 70:
                paint.change_mode('er')
            elif 600 <= pos_x <= 640 and 30 <= pos_y <= 70:
                paint.color = 'white'
            elif 650 <= pos_x <= 690 and 30 <= pos_y <= 70:
                paint.color = 'black'
            elif 700 <= pos_x <= 740 and 30 <= pos_y <= 70:
                paint.color = 'red'
            elif 750 <= pos_x <= 790 and 30 <= pos_y <= 70:
                paint.color = 'green'
            elif 800 <= pos_x <= 840 and 30 <= pos_y <= 70:
                paint.color = 'blue'
            else:
                paint.isdraw = True
        if event.type == pygame.MOUSEBUTTONUP:
            paint.isdraw = False
    paint.draw()
    pygame.display.update()
pygame.quit()