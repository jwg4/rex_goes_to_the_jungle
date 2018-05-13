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
    
    def compare_distance(self, point, radius):
        p_x, p_y = point
        d_x = p_x - self.rex_location[0]
        d_y = p_y - self.rex_location[1]
        if d_x ** 2 + d_y ** 2 < radius ** 2:
            return True
        else:
            return False

class MovementSequence(BaseSequence):
    SPEED = 5

    def handle_key(self, key):
        if (key == pygame.K_LEFT):
            if self.rex_location[0] > self.SPEED:
                self.rex_location = (self.rex_location[0] - self.SPEED, self.rex_location[1])
        elif (key == pygame.K_RIGHT):
            if self.rex_location[0] < self.window.dimensions[0] - self.SPEED:
                self.rex_location = (self.rex_location[0] + self.SPEED, self.rex_location[1])
        if (key == pygame.K_UP):
            if self.rex_location[1] > self.SPEED:
                self.rex_location = (self.rex_location[0], self.rex_location[1] - self.SPEED)
        elif (key == pygame.K_DOWN):
            if self.rex_location[1] < self.window.dimensions[1] - self.SPEED:
                self.rex_location = (self.rex_location[0], self.rex_location[1] + self.SPEED)
        self.handle_location()

    def handle_location(self):
        pass

class CaveSequence(MovementSequence):
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
    
    def handle_location(self):
        if self.compare_distance(self.window.center, self.SPEED * 2):
            self.in_portal = True

class JungleSequence(MovementSequence):
    def __init__(self, window):
        self.window = window
        self.background = pygame.image.load("img/bg/jungle.png")
    
    def init(self):
        self.rex_location = self.window.center

    def draw_background(self):
        self.window.window.blit(self.background, (0, 0))


class PortalSequence(BaseSequence):
    def init(self):
        self.rex_location = self.window.center
        self.portal_count = 0
        pygame.mixer.music.load("music/portal.ogg")
        pygame.mixer.music.play(-1)
    
    def draw_background(self):
        self.window.window.fill((0, 0, 0))
        portal_offset = self.portal_count % (2 * portal.WIDTH)
        for i in range(0, self.window.dimensions[0] // (2 * portal.WIDTH) + 2):
            k = i * 2 + 1
            r = portal_offset + k * portal.WIDTH
            color = random.choice(portal.COLORS)
            pygame.draw.circle(self.window.window, color, self.window.center, r, portal.WIDTH)
        self.portal_count = self.portal_count + 1

    @property
    def state(self):
        if self.portal_count > 25 * 10:
            return "JUNGLE"
        return None
