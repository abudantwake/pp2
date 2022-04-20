import pygame #importing require stuff
pygame.init()

#window settings
WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint 2.0')
FONT = pygame.font.SysFont('Arial', 25)

#Brush class
class Brush:
    def __init__(self):
        self.isdraw = False
        self.mode = 'rb'
        self.r = 10
        self.g = 10
        self.b = 10

    #drawing with modes and color
    def draw(self, pos):
        self.color = (int((self.r-10)/80 * 255), int((self.g-10)/80 * 255), int((self.b-10)/80 * 255))
        if self.isdraw:
            if self.mode == 'circle':
                pygame.draw.circle(WIN, self.color, pos, 20)
            if self.mode == 'rect':
                pygame.draw.rect(WIN, self.color, (pos[0]-25, pos[1]- 25, 50, 50))
            if self.mode == 'era':
                pygame.draw.circle(WIN, 'white', pos, 20)
            if self.mode == 'et':
                pygame.draw.polygon(WIN, self.color, [(pos[0],pos[1]-20), (pos[0]+20, pos[1]+20), (pos[0]-20, pos[1]+20)])
            if self.mode == 'rt':
                pygame.draw.polygon(WIN, self.color, [(pos[0]+20,pos[1]-30), (pos[0]+20, pos[1]+20), (pos[0]-20, pos[1]+20)])
            if self.mode == 'rb':
                pygame.draw.polygon(WIN, self.color, [(pos[0],pos[1]-30), (pos[0]+20, pos[1]), (pos[0],pos[1]+30), (pos[0]-20, pos[1])])
        self.table()
        self.cdio(self.r, self.g, self.b)#

    #panel to change the brush
    def table(self):
        pygame.draw.rect(WIN, 'grey', (0, 0, WIDTH, 100))
        pygame.draw.rect(WIN, 'black', (0, 0, WIDTH, 100), 2)
        self.button((50, 32), 'blue')
        self.button((106, 32), 'green')
        self.button((162, 32), 'red')
        self.button((218, 32), self.color, ' Cu')
        self.button((500, 32), 'white', ' S')
        self.button((556, 32), 'white', ' C')
        self.button((612, 32), 'white', ' Er')
        self.button((668, 32), 'white', ' Et')
        self.button((724, 32), 'white', ' Rt')
        self.button((780, 32), 'white', ' Rb')

    #panel to change the color
    def cdio(self, pos_r, pos_g, pos_b):
        pygame.draw.rect(WIN, 'grey', (0, HEIGHT-100, 100, 100))
        pygame.draw.line(WIN, 'white', (10, HEIGHT- 80), (90, HEIGHT - 80), 5)
        pygame.draw.line(WIN, 'white', (10, HEIGHT- 60), (90, HEIGHT - 60), 5)
        pygame.draw.line(WIN, 'white', (10, HEIGHT- 40), (90, HEIGHT - 40), 5)
        pygame.draw.line(WIN, 'red', (10, HEIGHT- 80), (pos_r, HEIGHT - 80), 5)
        pygame.draw.rect(WIN, 'red', (pos_r-5, HEIGHT - 90, 10, 20))
        pygame.draw.line(WIN, 'green', (10, HEIGHT- 60), (pos_g, HEIGHT - 60), 5)
        pygame.draw.rect(WIN, 'green', (pos_g-5, HEIGHT - 70, 10, 20))
        pygame.draw.line(WIN, 'blue', (10, HEIGHT- 40), (pos_b, HEIGHT - 40), 5)
        pygame.draw.rect(WIN, 'blue', (pos_b-5, HEIGHT - 50, 10, 20))

    #function that makes buttons
    def button(self, pos, color, text = ''):
        pygame.draw.rect(WIN, color, (*pos, 36, 36))
        pygame.draw.rect(WIN, 'black', (*pos, 36, 36), 2)
        if text == ' Er' or text == ' Cu':
            t = FONT.render(text, 1, 'black')
            WIN.blit(t, pos)
        elif text == ' S':
            pygame.draw.rect(WIN, 'black', (pos[0]+8, pos[1]+8, 20, 20))
        elif text == ' C':
            pygame.draw.circle(WIN, 'black', (pos[0]+18, pos[1]+18), 10)
        elif text == ' Et':
            pygame.draw.polygon(WIN, 'black', [(pos[0]+18, pos[1]+4), (pos[0]+4, pos[1]+30), (pos[0]+32, pos[1]+30)])
        elif text == ' Rt':
            pygame.draw.polygon(WIN, 'black', [(pos[0]+28, pos[1]+4), (pos[0]+8, pos[1]+30), (pos[0]+28, pos[1]+30)])
        elif text == ' Rb':
            pygame.draw.polygon(WIN, 'black', [(pos[0]+18, pos[1]+4), (pos[0]+8, pos[1]+18), (pos[0]+18, pos[1]+32), (pos[0]+28, pos[1]+18)])

#main loop
run = True
WIN.fill('white')
brush = Brush()
while run:
    #event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            #checking if we push the button
            if 32 <= mouse_pos[1] <= 68:
                if  50 <= mouse_pos[0] <= 86:
                    brush.r, brush.g, brush.b = 10, 10, 90
                if  106 <= mouse_pos[0] <= 142:
                    brush.r, brush.g, brush.b = 10, 90, 10
                if  162 <= mouse_pos[0] <= 198:
                    brush.r, brush.g, brush.b = 90, 10, 10
                if 500 <= mouse_pos[0] <= 536:
                    brush.mode = 'rect'
                if 556 <= mouse_pos[0] <= 592:
                    brush.mode = 'circle'
                if 612 <= mouse_pos[0] <= 648:
                    brush.mode = 'era'
                if 668 <= mouse_pos[0] <= 704:
                    brush.mode = 'et'
                if 724 <= mouse_pos[0] <= 760:
                    brush.mode = 'rt'
                if 780 <= mouse_pos[0] <= 816:
                    brush.mode = 'rb'
            elif 10 <= mouse_pos[0] <= 90 and HEIGHT-85 <= mouse_pos[1] <= HEIGHT-75:
                brush.r = mouse_pos[0]
            elif 10 <= mouse_pos[0] <= 90 and HEIGHT-65 <= mouse_pos[1] <= HEIGHT-55:
                brush.g = mouse_pos[0]
            elif 10 <= mouse_pos[0] <= 90 and HEIGHT-45 <= mouse_pos[1] <= HEIGHT-35:
                brush.b = mouse_pos[0]
            else:
                brush.isdraw = True
        if event.type == pygame.MOUSEBUTTONUP:
            brush.isdraw = False

    #draw
    mouse_pos = pygame.mouse.get_pos()
    brush.draw(mouse_pos)

    pygame.display.update()

pygame.quit()