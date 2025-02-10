import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(("Barman Game"))

background = pygame.image.load("../assets/background.jpg")
barman = pygame.image.load("../assets/barman.jpg")

barman_x = SCREEN_WIDTH // 2 - 100
barman_y = SCREEN_HEIGHT - 350

# boucle du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))  # Dessiner le background en premier
    screen.blit(barman, (barman_x, barman_y))  # Dessiner le barman par-dessus

    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()