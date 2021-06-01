import pygame
from network import Network


class Game:

    def __init__(self, w, h):
        #self.net = Network()
        self.width = w
        self.height = h
        self.canvas = FenetreConnexion(self.width, self.height, "FenetreConnexion")

    def button(self, screen, position, text):
        font = pygame.font.SysFont("Arial", 50)
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
        return screen.blit(text_render, (x, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)

            # Update Canvas
            self.canvas.draw_background()
            b1 = self.button(self.canvas.screen, (200, 200), 'connexion')
            self.canvas.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()




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
