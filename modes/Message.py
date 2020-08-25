import pygame
from pygame.font import Font


from datetime import datetime, timedelta

from .BaseMode import BaseMode

class Message(BaseMode):

    _render = None
    _font = None

    _run_until = None

    def _render_text(self, text):
        self._render.fill((0,0,0,255))

        rendered_text = self._font.render(text, True, (0,255,0))

        # work top and lef
        t_left = self.size[0]//2  - rendered_text.get_width()//2
        t_top = self.size[1]//2 - rendered_text.get_height()//2

        self._render.blit(rendered_text, (t_left, t_top))

    def enter_screen(self):
        if self._render == None:
            self._render = pygame.Surface(self.size, pygame.SRCALPHA)
            self._font = Font('assets/fonts/TerminusTTF-Bold-4.47.0.ttf', 72) # FIXME: do maths for font size

            self._render_text("Hello! No text given")
        
        self._run_until = datetime.now() + timedelta(seconds=3)

    def handle_event(self, event):
        # FIXME: only look at things with message
        try:
            self._render_text(event.message)
        except Exception as e:
            print(e)
            self._render_text("Bad Message")

    def render(self):
        
        if self._run_until < datetime.now():
            event_type = self.clacks.custom_events['RESUME']
            ev = pygame.event.Event(event_type)

            pygame.event.post(ev)
        
        return self._render