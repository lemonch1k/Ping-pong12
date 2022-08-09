from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((1200, 720))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('back.png'), (1200, 720))


game = True
clock = time.Clock()
FPS = 60
life = 10

font.init()
font1 = font.SysFont('Arial', 40)
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed

racket1 = Player('back.png', 5, 200, 30, 60, 10)
racket2 = Player('back.png', 650, 300, 30, 60, 10)
ball = GameSprite('back.png', 100, 300, 50, 50, 10)
run = True
finish = False
while run:
    window.blit(background, (0,0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
