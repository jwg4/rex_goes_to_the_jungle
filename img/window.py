import pygame
import sys

from dimensions import IMAGE_DIMENSIONS, WINDOW_DIMENSIONS


class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = IMAGE_DIMENSIONS
        self.scaled_dimensions = WINDOW_DIMENSIONS
        self.real_window = pygame.display.set_mode(self.scaled_dimensions)
        self.window = pygame.Surface(self.dimensions)
        self.clock = pygame.time.Clock()
        self.init_rex()
        self.draw()

    def init_rex(self):
        self.rex_location = (self.dimensions[0] / 2, self.dimensions[1] / 2)
        self.rex_image = pygame.image.load("img/REX.png")
    
    def main(self):
        self.clock.tick(40)
        self.listen_for_input()
        self.draw()
    
    def draw(self):
        self.draw_background()
        self.draw_rex()
        self.real_window.blit(pygame.transform.scale(self.window, self.scaled_dimensions), (0, 0))

    def draw_rex(self):
        self.window.blit(self.rex_image, self.rex_location)
    
    def draw_background(self):
        self.window.fill((0, 0, 0))