import pygame
import sys

# Initialize pygame
pygame.init

# Window Display
pygame.display.set_caption('Trash Signal Collecor')

# Create Screen
screen = pygame.display.set_mode((900, 700))

# Background
background = pygame.image.load("background.png")

# Player (Trash Can)
playerImg = pygame.image.load('game-images/trash-bin.png')
playerX = 370
playerY = 480
playerX_change = 0

clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(
                sys.exit()
            )

    pygame.display.update()
