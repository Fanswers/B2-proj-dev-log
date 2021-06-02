import pygame
from network import Network


class Game:

    def __init__(self, w, h):
        #self.net = Network()
        self.width = w
        self.height = h
        self.canvas = FenetreDeJeu(self.width, self.height, "FenetreDeJeu")

    def run(self):
        self.canvas.draw_background()

        clock = pygame.time.Clock()
        run = True
        rond = pygame.image.load("img/rond.png")
        rond = pygame.transform.scale(rond, (120, 120))
        croix = pygame.image.load("img/croix.png")
        croix = pygame.transform.scale(croix, (180, 180))
        player1 = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.K_ESCAPE:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pos = pygame.mouse.get_pos()
                        print(pos)
                        if pos[0] < 166:
                            if pos[1] < 166:
                                if player1:
                                    self.canvas.screen.blit(rond, (25, 25))
                                else:
                                    self.canvas.screen.blit(croix, (0, 0))
                            elif pos[1] <= 332:
                                self.canvas.screen.blit(rond, (25, 191))
                            elif pos[1] > 332:
                                self.canvas.screen.blit(rond, (25, 357))
                        elif pos[0] < 332:
                            if pos[1] < 166:
                                self.canvas.screen.blit(croix, (166, 0))
                            elif pos[1] <= 332:
                                self.canvas.screen.blit(croix, (166, 166))
                            elif pos[1] > 332:
                                self.canvas.screen.blit(croix, (166, 332))
                        elif pos[0] > 332:
                            if pos[1] < 166:
                                self.canvas.screen.blit(croix, (332, 0))
                            elif pos[1] <= 332:
                                self.canvas.screen.blit(croix, (332, 166))
                            elif pos[1] > 332:
                                self.canvas.screen.blit(croix, (332, 332))

            # Update Canvas
            self.canvas.update()

    def update_grille(self, grille, rond, croix):
        for i in range(len(grille)):
            if grille[i] == 1:
                if i == 0:
                    self.canvas.screen.blit(rond, (25, 25))
                elif i == 1:
                    self.canvas.screen.blit(rond, (25, 191))
                elif i == 2:
                    self.canvas.screen.blit(rond, (25, 357))
                elif i == 3:
                    self.canvas.screen.blit(rond, (191, 25))
                elif i == 4:
                    self.canvas.screen.blit(rond, (191, 191))
                elif i == 5:
                    self.canvas.screen.blit(rond, (191, 357))
                elif i == 6:
                    self.canvas.screen.blit(rond, (357, 25))
                elif i == 7:
                    self.canvas.screen.blit(rond, (357, 191))
                elif i == 8:
                    self.canvas.screen.blit(rond, (357, 357))
            if grille[i] == 2:
                if i == 0:
                    self.canvas.screen.blit(croix, (0, 0))
                if i == 1:
                    self.canvas.screen.blit(croix, (0, 166))
                if i == 2:
                    self.canvas.screen.blit(croix, (0, 332))
                if i == 3:
                    self.canvas.screen.blit(croix, (166, 0))
                if i == 4:
                    self.canvas.screen.blit(croix, (166, 166))
                if i == 5:
                    self.canvas.screen.blit(croix, (166, 332))
                if i == 6:
                    self.canvas.screen.blit(croix, (332, 0))
                if i == 7:
                    self.canvas.screen.blit(croix, (332, 166))
                if i == 8:
                    self.canvas.screen.blit(croix, (332, 332))
                    
    def chek_win(self, grille):
        i = 0
        while i < 9:
            if grille[i] == 1:
                if grille[i] == grille[i+1] == grille[i+2]:
                    print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+1] == grille[i+2]:
                    print("Victoire du joueur 2")
            i += 3

        i = 0
        while i < 3:
            if grille[i] == 1:
                if grille[i] == grille[i+3] == grille[i+6]:
                    print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+3] == grille[i+6]:
                    print("Victoire du joueur 2")
            i += 1

        i = 0
        while i < 1:
            if grille[i] == 1:
                if grille[i] == grille[i+4] == grille[i+8]:
                    print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+4] == grille[i+8]:
                    print("Victoire du joueur 2")
            i += 2

        i = 2
        while i < 3:
            if grille[i] == 1:
                if grille[i] == grille[i+2] == grille[i+4]:
                    print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+2] == grille[i+4]:
                    print("Victoire du joueur 2")
            i += 2


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

class FenetreDeJeu:

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
        pygame.draw.line(self.screen, (0, 0, 0), (166, 20), (166, 480), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (332, 20), (332, 480), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (20, 166), (480, 166), 2)
        pygame.draw.line(self.screen, (0, 0, 0), (20, 332), (480, 332), 2)
