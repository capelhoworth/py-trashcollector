import pygame
import sys

# Initialize pygame
pygame.init

# Window Display
pygame.display.set_caption('Trash Signal Collecor')

# Create Screen
screen = pygame.display.set_mode((940, 780))

# Background
background = pygame.image.load("background.png")

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
    clock.tick(60)
