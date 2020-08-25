import pygame
from pygame.time import Clock

from clacks import Clacks

pygame.init()

width = 1920
height = 1080

clacks = Clacks()

clacks.clock = Clock()

screen = pygame.display.set_mode((width,height), display=2)

# Part 1 - Initial Setup and throw something on the screen

from modes.LogoOne import LogoOne

current_screen = LogoOne(clacks, (width,height))

screens = {
    "Logo": current_screen
}
screens['Logo'].enter_screen()
screen.blit(screens['Logo'].render(), (0,0))
pygame.display.flip()

# Part 2 - now load everything else

for key,val in clacks.custom_events.items():
    clacks.custom_events[key] = pygame.event.custom_type()

from modes.Message import Message
screens['Message'] = Message(clacks, (width, height))

import webserver

webserver.run_webserver(clacks)

# Part 3 - enter the mega loop

while clacks.alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye Bye")
            pygame.display.quit()
            clacks.alive = False

        if event.type == pygame.KEYDOWN:
            print("KEy pressed - closing")
            pygame.display.quit()
            clacks.alive = False

        if event.type == clacks.custom_events['MESSAGE']:
            print("Message! flipping to message")
            current_screen.exit_screen()
            current_screen = screens['Message']
            current_screen.enter_screen()
            current_screen.handle_event(event)

        if event.type == clacks.custom_events['RESUME']:
            print("Message! flipping to message")
            current_screen.exit_screen()
            current_screen = screens['Logo']
            current_screen.enter_screen()
            current_screen.handle_event(event)
            

    if clacks.alive:
        screen.fill((0,0,0))
        screen.blit(current_screen.render(), (0,0))
        pygame.display.flip()
        clacks.clock.tick(15)