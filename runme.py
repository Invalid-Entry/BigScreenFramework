import pygame
from pygame.time import Clock

import random

width = 1920
height = 1080

clock = Clock()

screen = pygame.display.set_mode((width,height))


back = pygame.image.load("assets/lightning/ie-1.png")

inner = [
    pygame.image.load("assets/lightning/i-1.png"),
    pygame.image.load("assets/lightning/i-2.png"),
    pygame.image.load("assets/lightning/i-3.png")
]

outer = [
    pygame.image.load("assets/lightning/o-1.png"),
    pygame.image.load("assets/lightning/o-2.png"),
    pygame.image.load("assets/lightning/o-3.png")
]

ul = [
    pygame.image.load("assets/lightning/ul-1.png"),
    pygame.image.load("assets/lightning/ul-2.png"),
    pygame.image.load("assets/lightning/ul-3.png")
]

ur = [
    pygame.image.load("assets/lightning/ur-1.png"),
    pygame.image.load("assets/lightning/ur-2.png"),
    pygame.image.load("assets/lightning/ur-3.png")
]

ll = [
    pygame.image.load("assets/lightning/ll-1.png"),
    pygame.image.load("assets/lightning/ll-2.png"),
    pygame.image.load("assets/lightning/ll-3.png")
]

lr = [
    pygame.image.load("assets/lightning/lr-1.png"),
    pygame.image.load("assets/lightning/lr-2.png"),
    pygame.image.load("assets/lightning/lr-3.png")
]

upper_left = 0
lower_left = 0
lower_right = 0
upper_right = 0

alive = True


def lightning(screen, control, images):
    if control == 0:
        if random.random() > 0.95:
                control = random.choice((3,5,7))

    else:
        control += random.choice((0,0,0,0,0,0,0,0,1,2,3))

    if control > 0:
        
        options = ( (True, False, False), (False, True, False), (False, False, True),
                    (True, True, False), (True, False, True), (False, True, True),
                    (True, True, True) )
        this_time = random.choice(options)

        for x in range(3):
            if this_time[x]:
                screen.blit(images[x], (0,0))

        control -= 1
    return control

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye")
            pygame.display.quit()
            alive = False

        if event.type == pygame.KEYDOWN:
            print("KEy pressed - closing")
            pygame.display.quit()
            alive = False

    if alive:
        screen.fill((0,0,0))

        # Fill out here
        screen.blit(back, (0,0))

        for img in inner:
            if random.random() > 0.1:
                screen.blit(img, (0,0))

        for img in outer:
            if random.random() > 0.1:
                screen.blit(img, (0,0))

        upper_left = lightning(screen, upper_left, ul)
        upper_right = lightning(screen, upper_right, ur)
        lower_left = lightning(screen, lower_left, ll)
        lower_right = lightning(screen, lower_right, lr)

        pygame.display.flip()
        clock.tick(15)