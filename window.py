import pygame
import sys

from dimensions import IMAGE_DIMENSIONS, WINDOW_DIMENSIONS


class Window(object):
    def __init__(self):
        # Create the window/Initialise
        self.dimensions = IMAGE_DIMENSIONS
        self.center = (self.dimensions[0] // 2, self.dimensions[1] // 2)
        self.scaled_dimensions = WINDOW_DIMENSIONS
        self.real_window = pygame.display.set_mode(self.scaled_dimensions)
        self.window = pygame.Surface(self.dimensions)
        self.clock = pygame.time.Clock()
        self.portal_offset = 0
        self.init_rex()
        self.draw()

    def init_rex(self):
        self.rex_location = self.center
        self.rex_image = pygame.image.load("img/REX.png")
        self.rex_shift = (self.rex_image.get_width() // 2, self.rex_image.get_height() // 2)
    
    def main(self):
        self.clock.tick(40)
        self.listen_for_input()
        self.draw()
    
    def draw(self):
        self.draw_background()
        self.draw_rex()
        self.real_window.blit(pygame.transform.scale(self.window, self.scaled_dimensions), (0, 0))

    def draw_rex(self):
        location = (
            self.rex_location[0] - self.rex_shift[0],
            self.rex_location[1] - self.rex_shift[1]
        )
        self.window.blit(self.rex_image, location)
    
    def draw_background(self):
        WIDTH = 20
        self.window.fill((0, 0, 0))
        for i in range(1, self.dimensions[0] // (2 * WIDTH) + 2):
            r = self.portal_offset + i * 2 * WIDTH
            pygame.draw.circle(self.window, (128, 128, 128), self.center, r, WIDTH)
        self.portal_offset = (self.portal_offset + 1) % (2 * WIDTH)

    def handle_key(self, key):
        pass

    def handle_key_up(self, key):
        pass

    def quit(self):
        pygame.quit()
        sys.exit()

    def listen_for_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                self.handle_key(event.key)
            elif event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYUP:  # Keyboard
                self.handle_key_up(event.key)
