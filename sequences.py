import random

import pygame

import portal

class BaseSequence(object):
    def __init__(self, window):
        self.window = window
    
    def draw(self):
        self.draw_background()
        self.draw_rex()
        return self.state

    @property
    def state(self):
        return None

    def draw_rex(self):
        location = (
            self.rex_location[0] - self.window.rex_shift[0],
            self.rex_location[1] - self.window.rex_shift[1]
        )
        self.window.window.blit(self.window.rex_image, location)

    def handle_key(self, key):
        pass

    def handle_key_up(self, key):
        pass


class CaveSequence(BaseSequence):
    SPEED = 5

    def init(self):
        self.rex_location = self.window.rex_shift
        self.in_portal = False

    def draw_background(self):
        self.window.window.fill((30, 200, 40))
        color = random.choice(portal.COLORS)
        pygame.draw.circle(self.window.window, color, self.window.center, portal.WIDTH * 3, portal.WIDTH)

    @property
    def state(self):
        if self.in_portal:
            return 'PORTAL'

    def handle_key(self, key):
        if (key == pygame.K_LEFT):
            if self.rex_location[0] > self.SPEED:
                self.rex_location = (self.rex_location[0] - self.SPEED, self.rex_location[1])
        elif (key == pygame.K_RIGHT):
            if self.rex_location[0] < self.window.dimensions[0] - self.SPEED:
                self.rex_location = (self.rex_location[0] + self.SPEED, self.rex_location[1])
        if (key == pygame.K_DOWN):
            if self.rex_location[1] > self.SPEED:
                self.rex_location = (self.rex_location[0], self.rex_location[1] - self.SPEED)
        elif (key == pygame.K_UP):
            if self.rex_location[1] < self.window.dimensions[1] - self.SPEED:
                self.rex_location = (self.rex_location[0], self.rex_location[1] + self.SPEED)
        if (self.rex_location[0] ** 2 + self.rex_location[1] ** 2 < 4 * self.SPEED ** 2):
            self.in_portal = True

class PortalSequence(BaseSequence):
    def init(self):
        self.rex_location = self.window.center
        self.portal_offset = 0
        pygame.mixer.music.load("music/portal.ogg")
        pygame.mixer.music.play(-1)
    
    def draw_background(self):
        self.window.window.fill((0, 0, 0))
        for i in range(0, self.window.dimensions[0] // (2 * portal.WIDTH) + 2):
            k = i * 2 + 1
            r = self.portal_offset + k * portal.WIDTH
            color = random.choice(portal.COLORS)
            pygame.draw.circle(self.window.window, color, self.window.center, r, portal.WIDTH)
        self.portal_offset = (self.portal_offset + 1) % (2 * portal.WIDTH)

