import pygame

from .BaseMode import BaseMode


class LogoOne(BaseMode):

    _render = None

    def enter_screen(self):
        if self._render == None:
            self._render = pygame.image.load("assets/lightning/ie-1.png")

    def render(self):
        return self._render
