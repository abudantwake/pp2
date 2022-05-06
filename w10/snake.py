import pygame
import psycopg2
import json
from random import randrange

pygame.init()

config = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    port = 5432,
    user = "postgres",
    password = "superuser123"
)

current = config.cursor()

level = 1
mon = 800
size = 50
fps = 60
bg = pygame.image.load("game_background.png")
bg = pygame.transform.scale(bg, (800, 800))
x, y = 300, 300
length = 1
snake = [(x, y)]


print("What is your name?")
username = input()

select = '''
    SELECT * FROM savefile WHERE user_name = %s;
'''
current.execute(select, [username])
DICT = current.fetchone()


if DICT == None:
    insert = '''
        INSERT INTO savefile VALUES(%s, 0, 0);
    '''
    current.execute(insert, [username])
    config.commit()
pygame.init()

current.execute(select, [username])
DICT = current.fetchone()


buttons = {
    'w': True,
    'a': True,
    'd': True,
    's': True
}

front = pygame.font.SysFont('Ariel', 26, True)
count = 0

walls = {  # уровни препятствий,
    1: [(50, 50), (50, 100), (50, 150), (50, 200), (150, 0), (200, 0), (250, 0), (500, 500), (550, 500), (500, 550),
        (600, 500), (650, 500)],
    2: [(700, 700), (650, 700), (700, 650), (600, 700), (700, 600), (700, 550), (650, 550), (650, 500)],
    3: [(0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0), (450, 0), (500, 0),
        (550, 0), (600, 0), (650, 0), (700, 0), (0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350),
        (0, 400), (0, 450), (0, 500), (0, 550), (0, 600), (0, 650), (0, 700)]
}

speed = 7
sup = 10  # чтобы узнать попадает ли score в range
score = 0
dx, dy = 0, 0

clock = pygame.time.Clock()
time = 50

apple = randrange(50, mon, size), randrange(0, mon, size)

while apple in walls:
    apple = randrange(50, mon, size), randrange(0, mon, size)

level1 = 9
level2 = 20

screen = pygame.display.set_mode([mon, mon])

score_font = pygame.font.SysFont("Verdana", 20)

restart = True
SCORE = 0
HIGHSCORE = DICT[1]
LEVEL = DICT[2]
working = True
while working:
    SCORE = 0
    pause = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
#Нужно для проверки чтобы если мы идем на право то не могли идти на лево, если на верх то вниз
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and buttons['w']:
                buttons = {
                    'w': True,
                    'a': True,
                    'd': True,
                    's': False
                }
                dx, dy = 0, -1
            elif event.key == pygame.K_s and buttons['s']:
                dx, dy = 0, 1
                buttons = {
                    'w': False,
                    'a': True,
                    'd': True,
                    's': True
                }
            elif event.key == pygame.K_a and buttons['a']:
                dx, dy = -1, 0
                buttons = {
                    'w': True,
                    'a': True,
                    'd': False,
                    's': True
                }
            elif event.key == pygame.K_d and buttons['d']:
                dx, dy = 1, 0
                buttons = {
                    'w': True,
                    'a': False,
                    'd': True,
                    's': True
                }
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                sql = '''
                            UPDATE savefile SET score = %s, level = %s WHERE user_name = %s;
                            '''
                current.execute(sql, [SCORE, LEVEL, username])
                config.commit()
                pause = True

    screen.blit(bg, (0, 0))
#если змейка ударяется об стену то игра заканчивается
    if snake[-1] in walls[level]:
     
       pygame.quit()
    #if apple in walls[level]:  # нужна для проверки если яблоко появилось внутри стеn

