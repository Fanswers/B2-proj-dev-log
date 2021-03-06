import pygame
from network import Network


class Player():
    def __init__(self, NOM, PRENOM, ID, LEVEL, WIN, LOOSE):
        self.nom = NOM
        self.prenom = PRENOM
        self.id = ID
        self.level = LEVEL
        self.win = WIN
        self.loose = LOOSE


class Connexion:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.canvas = FenetreConnexion(self.width, self.height, "FenetreDeConnexion")

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
            b1 = self.button(self.canvas.screen, (50, 200), 'Rechercher une partie')
            self.canvas.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        g = Game(500,500)
                        g.run()

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

class Game:
    def __init__(self, w, h):
        self.net = Network()
        self.width = w
        self.height = h
        self.canvas = FenetreDeJeu(self.width, self.height, "FenetreDeJeu")
        self.grille = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.tour = 0

    def run(self):
        self.canvas.draw_background()
        clock = pygame.time.Clock()
        run = True

        # Initialisation des images
        rond = pygame.image.load("img/rond.png")
        rond = pygame.transform.scale(rond, (120, 120))
        croix = pygame.image.load("img/croix.png")
        croix = pygame.transform.scale(croix, (180, 180))

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.net.client.close()
                    c = Connexion(500,500)
                    c.run()

                if event.type == pygame.K_ESCAPE:
                    run = False
                    self.net.client.close()
                    c = Connexion(500, 500)
                    c.run()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos = pygame.mouse.get_pos()

                    if pos[0] < 166:
                        if pos[1] < 166:
                            if self.net.id == '1' and self.grille[0] == 0 and self.tour == 1:
                                self.grille[0] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[0] == 0 and self.tour == 0:
                                self.grille[0] = 2
                                self.tour = 1
                        elif pos[1] <= 332:
                            if self.net.id == '1' and self.grille[1] == 0 and self.tour == 1:
                                self.grille[1] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[1] == 0 and self.tour == 0:
                                self.grille[1] = 2
                                self.tour = 1
                        elif pos[1] > 332:
                            if self.net.id == '1' and self.grille[2] == 0 and self.tour == 1:
                                self.grille[2] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[2] == 0 and self.tour == 0:
                                self.grille[2] = 2
                                self.tour = 1
                    elif pos[0] < 332:
                        if pos[1] < 166:
                            if self.net.id == '1' and self.grille[3] == 0 and self.tour == 1:
                                self.grille[3] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[3] == 0 and self.tour == 0:
                                self.grille[3] = 2
                                self.tour = 1
                        elif pos[1] <= 332:
                            if self.net.id == '1' and self.grille[4] == 0 and self.tour == 1:
                                self.grille[4] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[4] == 0 and self.tour == 0:
                                self.grille[4] = 2
                                self.tour = 1
                        elif pos[1] > 332:
                            if self.net.id == '1' and self.grille[5] == 0 and self.tour == 1:
                                self.grille[5] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[5] == 0 and self.tour == 0:
                                self.grille[5] = 2
                                self.tour = 1
                    elif pos[0] > 332:
                        if pos[1] < 166:
                            if self.net.id == '1' and self.grille[6] == 0 and self.tour == 1:
                                self.grille[6] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[6] == 0 and self.tour == 0:
                                self.grille[6] = 2
                                self.tour = 1
                        elif pos[1] <= 332:
                            if self.net.id == '1' and self.grille[7] == 0 and self.tour == 1:
                                self.grille[7] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[7] == 0 and self.tour == 0:
                                self.grille[7] = 2
                                self.tour = 1
                        elif pos[1] > 332:
                            if self.net.id == '1' and self.grille[8] == 0 and self.tour == 1:
                                self.grille[8] = 1
                                self.tour = 0
                            elif self.net.id == '0' and self.grille[8] == 0 and self.tour == 0:
                                self.grille[8] = 2
                                self.tour = 1

            # Send Network Stuff
            grille, self.tour = self.parse_data(self.send_data())

            if grille != 5:
                for i in range(len(self.grille)):
                    self.grille[i] = int(grille[i])

            # Update Canvas
            self.update_grille(self.grille, rond, croix)
            self.chek_win(self.grille)
            self.canvas.update()
        pygame.quit()

    def send_data(self):
        """
        Send position to server
        :return: None
        """

        coup = str(self.net.id) + ":" + str(self.grille) + "/" + str(self.tour)
        reply = self.net.send(coup)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            grille = str(data.split(":")[1]).split("/")[0][1:-1].split(",")
            tour = str(data.split(":")[1]).split("/")[1]
            grille2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(grille2)):
                grille2[i] = int(grille[i])
            return grille2, int(tour)
        except:
            return 0

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
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (83 + (i * 55), 20), (83 + (i * 55), 480), 10)
                    return print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+1] == grille[i+2]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (83 + (i * 55), 20), (83 + (i * 55), 480), 10)
                    return print("Victoire du joueur 2")
            i += 3
        i = 0
        while i < 3:
            if grille[i] == 1:
                if grille[i] == grille[i+3] == grille[i+6]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (20, 83 + (i * 166)), (480, 83 + (i * 166)), 10)
                    return print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+3] == grille[i+6]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (20, 83 + (i * 166)), (480, 83 + (i * 166)), 10)
                    return print("Victoire du joueur 2")
            i += 1

        i = 0
        while i < 1:
            if grille[i] == 1:
                if grille[i] == grille[i+4] == grille[i+8]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (50, 50), (450, 450), 10)
                    return print("Victoire du joueur 1")

            if grille[i] == 2:
                if grille[i] == grille[i+4] == grille[i+8]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (50, 50), (450, 450), 10)
                    return print("Victoire du joueur 2")
            i += 2

        i = 2
        while i < 3:
            if grille[i] == 1:
                if grille[i] == grille[i+2] == grille[i+4]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (450, 50), (50, 450), 10)
                    return print("Victoire du joueur 1")
            if grille[i] == 2:
                if grille[i] == grille[i+2] == grille[i+4]:
                    pygame.draw.line(self.canvas.screen, (255, 0, 0), (450, 50), (50, 450), 10)
                    return print("Victoire du joueur 2")
            i += 2

        i = 0
        count = 0
        while i < 9:
            if grille[i] == 0:
                count += 1
            i += 1
        if count == 0:
            return print("Egalit?? !")



class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255,255,255))

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


