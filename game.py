import pygame
from network import Network


class Game:

    def __init__(self, w, h):
        #self.net = Network()
        self.width = w
        self.height = h
        self.canvas = FenetreConnexion(self.width, self.height, "FenetreConnexion")

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

            # Update Canvas
            self.canvas.draw_background()
            self.canvas.update()

class FenetreConnexion:

    def __init__(self, w, h, name=""):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255, 255, 255))