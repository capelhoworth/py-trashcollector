import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Initialize mixer
mixer.init()

# create the screen
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Window Display
pygame.display.set_caption("🗑️ Trash Signal Collector 🛜")
# icon = pygame.image.load('game-images/spaceship.png')
# pygame.display.set_icon(icon)

# Background
background = pygame.image.load("game-images/background.png")

# # Load audio files
# mixer.music.load('Sexy Scifi.wav')
# pew_sound = mixer.Sound('Pew.wav')
# boom_sound = mixer.Sound('Boom.wav')

# # Set initial volume levels
# theme_volume = 1.0
# pew_volume = 0.3
# boom_volume = 0.3
# pew_sound.set_volume(pew_volume)
# boom_sound.set_volume(boom_volume)

# # Play the theme sound with the initial volume
# mixer.music.set_volume(theme_volume)
# mixer.music.play(-1)

# Player
playerImg = pygame.image.load('game-images/trash-bin.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('game-images/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('game-images/laser.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

# Score Text
score_value = 0
font = pygame.font.Font('arcade.ttf', 50)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('arcade.ttf', 100)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))




def player(x, y): 
    screen.blit(playerImg, (x, y))


# def enemy(x, y, i): 
#     screen.blit(enemyImg[i], (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB parameters
    screen.fill((255, 0, 255))
    # Background Image
    screen.blit(background, (0, 0))
    # Draw buttons before other elements
    theme_playing_button.draw()
    sfx_playing_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # if keystroke is pressed, check if it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    pew_sound.set_volume(pew_volume)
                    pew_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # if mouse clicks mute buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if theme_playing_button.rect.collidepoint(event.pos):
                theme_playing_button.is_muted = not theme_playing_button.is_muted
                if theme_playing_button.is_muted:
                    mixer.music.set_volume(0)  # Mute the theme
                else:
                    mixer.music.set_volume(theme_volume)  # Unmute the theme

            if sfx_playing_button.rect.collidepoint(event.pos):
                sfx_playing_button.is_muted = not sfx_playing_button.is_muted
                if sfx_playing_button.is_muted:
                    pew_sound.set_volume(0)  # Mute sound effects
                    boom_sound.set_volume(0)
                else:
                    pew_sound.set_volume(pew_volume)  # Unmute sound effects
                    boom_sound.set_volume(boom_volume)


    # set player boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over Man, Game Over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(250, 250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            boom_sound.set_volume(boom_volume)
            boom_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()