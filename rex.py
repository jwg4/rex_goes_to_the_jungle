import pygame
from window import Window

if __name__ == "__main__":
    pygame.init()
    window = Window()

    while True:
        window.main()
        pygame.display.update()