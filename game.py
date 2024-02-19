from pygame import*
from random import randint
from time import time as time_count
window = display.set_mode()
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT or(e.type == KEYDOWN and e.key == K_ESCAPE):
            game = False
    display.update() 
    clock.tick(60)

