import pygame
import random
import sys

import portal
from dimensions import IMAGE_DIMENSIONS, WINDOW_DIMENSIONS
from sequences import CaveSequence, JungleSequence, PortalSequence


class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = IMAGE_DIMENSIONS
        self.center = (self.dimensions[0] // 2, self.dimensions[1] // 2)
        self.scaled_dimensions = WINDOW_DIMENSIONS
        self.real_window = pygame.display.set_mode(self.scaled_dimensions)
        self.window = pygame.Surface(self.dimensions)
        self.clock = pygame.time.Clock()
        self.init_rex()
        self.init_music()
        self.init_sequences()
        self.draw()

    def init_sequences(self):
        self.sequences = {
            'CAVE': CaveSequence(self),
            'JUNGLE': JungleSequence(self),
            'PORTAL': PortalSequence(self),
        }
        self.current_sequence = self.sequences['CAVE']
        self.current_sequence.init()

    def init_music(self):
        pygame.mixer.init()

    def init_rex(self):
        self.rex_image = pygame.image.load("img/sprites/REX.png")
        self.rex_shift = (self.rex_image.get_width() // 2, self.rex_image.get_height() // 2)
    
    def main(self):
        self.clock.tick(40)
        self.listen_for_input()
        self.draw()

    def draw(self):
        next_state = self.current_sequence.draw()
        self.real_window.blit(pygame.transform.scale(self.window, self.scaled_dimensions), (0, 0))
        if next_state:
            self.current_sequence.exit()
            self.current_sequence = self.sequences[next_state]
            self.current_sequence.init()

    def quit(self):
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

    def listen_for_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                self.current_sequence.handle_key(event.key)
            elif event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYUP:  # Keyboard
                self.current_sequence.handle_key_up(event.key)
