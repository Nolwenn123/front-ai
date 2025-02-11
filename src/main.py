import pygame
import numpy as np
import scipy.ndimage

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Barman Game")

# Charger l'image et l'adapter à la taille de l'écran
background_barman = pygame.image.load("../assets/background-barman.png")
background_barman = pygame.transform.scale(background_barman, (SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (223, 39, 0)

font = pygame.font.Font(None, 60)

# Définition des pages du jeu
STATE_MENU = "menu"
STATE_GAME = "game"
game_state = STATE_MENU

button_rect = pygame.Rect(400, 500, 200, 80)

# Convertir l'image en tableau pour appliquer un flou
def apply_blur(surface, sigma=5):
    """ Applique un flou gaussien à une surface pygame """
    array = pygame.surfarray.array3d(surface)  # Convertir l'image en tableau numpy
    blurred_array = scipy.ndimage.gaussian_filter(array, sigma=(sigma, sigma, 0))  # Appliquer le flou
    return pygame.surfarray.make_surface(blurred_array)  # Reconvertir en surface

# Créer l'image floutée une seule fois pour éviter de la recalculer à chaque frame
blurred_background = apply_blur(background_barman, sigma=5)

# Boucle du jeu
running = True
while running:
    screen.fill(WHITE)

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gérer le clic de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == STATE_MENU:  # Si on est dans le menu
                if button_rect.collidepoint(event.pos):  # Si on clique sur le bouton "Jouer"
                    game_state = STATE_GAME

    # Afficher le bon écran en fonction de l'état
    if game_state == STATE_MENU:
        screen.blit(blurred_background, (0, 0))  # Afficher l'image floutée

        # Dessiner le bouton
        pygame.draw.rect(screen, BLACK, button_rect, border_radius=10)
        text_surface = font.render("Jouer", True, WHITE)
        screen.blit(text_surface, (button_rect.x + 40, button_rect.y + 20))

    elif game_state == STATE_GAME:
        screen.blit(background_barman, (0, 0))

    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()
