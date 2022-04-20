import pygame
pygame.init()
from level import level_1, level_2
import random

#Parameters
font = pygame.font.SysFont('PixelTimes', 40)
font2 = pygame.font.SysFont('PixelTimes', 30)
tile_size = 40
screen_width, screen_height = len(level_1[0])*tile_size, len(level_1)*tile_size
screen = pygame.display.set_mode((screen_width + 200, screen_height))
pygame.display.set_caption("Zmeyka.kz")
background = pygame.image.load('images\grass.png')
background = pygame.transform.scale(background, (screen_width,screen_height))
clock = pygame.time.Clock()
tail_list = []
walls = []
food_list = []
FPS = 120
speed = 150
lvl = 1
pre_tail = pygame.Rect(0,0,0,0)
alive = True
levels = [level_1, level_2]
l_num = 0
wall_sp = pygame.sprite.Group()
food = pygame.image.load('images/apple.png')
food = pygame.transform.scale(food, (tile_size, tile_size))

#Classes
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, n = False):
        super().__init__()
        if n:
            self.image = pygame.image.load('images/wall_n.png')
        else:
            self.image = pygame.image.load('images/wall.png')
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft = pos)

class Snake:
    def __init__(self):
        self.speed = tile_size
        self.angle = 0
        self.ax = 0
        self.dir = 1
        self.l = 2
        self.head_1 = pygame.image.load('images/Head.png')
        self.head_1 = pygame.transform.scale(self.head_1, (tile_size, tile_size))
        self.head_2 = pygame.image.load('images/Head_eat.png')
        self.head_2 = pygame.transform.scale(self.head_2, (tile_size, tile_size))
        self.head_3 = pygame.image.load('images/Head_die.png')
        self.head_3 = pygame.transform.scale(self.head_3, (tile_size, tile_size))
        self.tail_im = pygame.image.load('images/Body_1.png')
        self.tail_im = pygame.transform.scale(self.tail_im, (tile_size, tile_size))

    def reset(self):
        self.angle = 0
        self.ax = 0
        self.dir = 1
        self.l = 2

    def head(self, pos):
        self.image = self.head_1
        self.rect = self.image.get_rect(topleft = pos)
    
    def draw(self):
        table(self.l)
        for n, i in enumerate(tail_list):
            screen.blit(self.tail_im, i)
        screen.blit(self.image, self.rect)

    def move(self):
        self.image = self.head_1
        if self.ax == 0:
            self.image = pygame.transform.rotate(self.head_1, -90 * self.dir)
            self.rect.move_ip(self.speed*self.dir, 0)
            self.angle = -90 * self.dir
        elif self.ax == 1:
            if self.dir == 1: self.angle = 180
            else: self.angle = 0
            self.image = pygame.transform.rotate(self.head_1, self.angle)
            self.rect.move_ip(0, self.speed*self.dir)
        self.collision()
        self.tail()

    def collision(self):
        if self.rect.top < 0 and self.dir < 0:
            self.rect.bottom = screen_height
        elif self.rect.bottom > screen_height and self.dir > 0:
            self.rect.top = 0
        elif self.rect.left < 0:
            self.rect.right = screen_width
        elif self.rect.right > screen_width:
            self.rect.left = 0

        if self.rect in walls:
            self.image = pygame.transform.rotate(self.head_3, self.angle)
            global alive
            alive = False

        if self.rect in food_list:
            food_list.remove(self.rect)
            self.image = pygame.transform.rotate(self.head_2, self.angle)
            self.l += 1

    def ch_dir(self, axis, dir):
        self.ax = axis
        self.dir = dir

    def tail(self):
        self.t_rect = self.image.get_rect(center = self.rect.center)
        if self.t_rect in tail_list:
            global alive
            alive = False
        if self.t_rect not in tail_list:
            tail_list.append((self.t_rect))
        if len(tail_list) > self.l:
            tail_list.pop(0)

        return tail_list

#Timers
SPAWN_FOOD = pygame.USEREVENT + 7
MOVE_SNAKE = pygame.USEREVENT + 6
def timers(sp, ms):
    pygame.time.set_timer(SPAWN_FOOD, 1000*sp)
    pygame.time.set_timer(MOVE_SNAKE, ms*2)

#Functions
def table(score):
    table = pygame.image.load('images/table.jpg')
    table = pygame.transform.scale(table, (200, screen_height))
    text_S = font.render(f'Score:  {score-2}', 1, 'white')
    if lvl < len(levels):
        text_L = font.render(f'Lvl:  {lvl}', 1, 'white')
    else:
        text_L = font.render(f'Lvl:  Max', 1, 'white')
    text_SP = font2.render(f'Speed:{round(1000/speed, 1)}b/s', 1, 'white')
    screen.blit(table, (screen_width, 0))
    screen.blit(text_S, (screen_width+10, 20))
    screen.blit(text_L, (screen_width+10, 80))
    screen.blit(text_SP, (screen_width+10, 140))

def food_sp():
    x = random.randint(1, screen_width/tile_size - 1) * tile_size
    y = random.randint(1, screen_height/tile_size - 1) * tile_size
    rect = food.get_rect(topleft = (x, y))
    if rect not in tail_list and rect not in walls and rect not in food_list:
        food_list.append(rect)

def set_lvl(level, snake, fs = False):
    for rows_n, rows in enumerate(level):
        for col_n, col in enumerate(rows):
            x = col_n * tile_size
            y = rows_n * tile_size
            if col == 'W':
                tile = Wall((x, y))
                walls.append(tile.rect)
                wall_sp.add(tile)
            if col == 'S' and fs:
                snake.head((x, y))
            if col == 'N' and not fs:
                tile = Wall((x, y), True)
                wall_sp.add(tile)

def reset():
    global alive, tail_list, lvl, wall_sp, walls, food_list, l_num, speed
    alive = True
    wall_sp.empty()
    walls = []
    set_lvl(level_1, snake, True)
    tail_list = []
    l_num = 0
    food_list = []
    snake.reset()
    lvl = 1
    speed = 150
    timers(3, speed)

def draw(sc):
    sc.blit(background, (0, 0))
    for rect in food_list:
        sc.blit(food, rect)
    
    for tile in wall_sp:
        sc.blit(tile.image, tile.rect)
    for tile in wall_sp:
        
        sc.blit(tile.image, tile.rect)

#Start settings
snake = Snake()
set_lvl(level_1, snake, True)
timers(3, speed)
st =True
run = True

#Main loop
while run:
    clock.tick(FPS)

    #Event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == SPAWN_FOOD and alive:
            food_sp()

        if event.type == MOVE_SNAKE and alive:
            snake.move()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.ax != 1:
                snake.ch_dir(1, -1)
            elif event.key == pygame.K_s and snake.ax != 1:
                snake.ch_dir(1, 1)
            elif event.key == pygame.K_d and snake.ax != 0:
                snake.ch_dir(0, 1)
            elif event.key == pygame.K_a and snake.ax != 0:
                snake.ch_dir(0, -1)
    #Level set
    if snake.l - 2 - (lvl-1)*4 >= 4:
        speed *= 0.9
        lvl += 1
        if l_num < len(levels):
            set_lvl(levels[l_num], snake)
            l_num += 1
        timers(3, int(speed))
    
    draw(screen)
    snake.draw()

    while st:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                st = False
                break
        text_s = font.render('Press any key to start!', 1, 'white')
        screen.blit(text_s, (screen_width/2 - text_s.get_width()/2, screen_height/2 - text_s.get_height()/2))
        pygame.display.update()

    if not alive:
        text_s = font.render('YOU Lost!', 1, 'white')
        screen.blit(text_s, (screen_width/2 - text_s.get_width()/2, screen_height/2 - text_s.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)
        reset()
        st = True
    pygame.display.flip()

pygame.quit()