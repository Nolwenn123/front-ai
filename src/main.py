import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(("Barman Game"))



background_barman = pygame.image.load("../assets/background-barman.png")
background_barman = pygame.transform.scale(background_barman, (SCREEN_WIDTH, SCREEN_HEIGHT))

# boucle du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_barman, (0,0))
    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()