import pygame
import os

WIDTH, HEIGHT = 700, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python vs Java")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
GRAVITY = 2

PYTHON_CHAR_IMAGE = pygame.image.load(os.path.join("data", "spaceship.png"))
PYTHON_CHAR = pygame.transform.scale(PYTHON_CHAR_IMAGE, (50, 50))
JAVA_CHAR_IMAGE = pygame.image.load(os.path.join("data", "spaceship.png"))
JAVA_CHAR = pygame.transform.scale(JAVA_CHAR_IMAGE, (50, 50))

def draw_window(python_player, java_player):
    WIN.fill(WHITE)
    WIN.blit(PYTHON_CHAR, (python_player.x, python_player.y))
    WIN.blit(JAVA_CHAR, (java_player.x, java_player.y))
    pygame.display.update()

def python_player_movement(keys_pressed, python_player):
        if keys_pressed[pygame.K_a] and python_player.x - VEL > 0:
            python_player.x -= VEL
        if keys_pressed[pygame.K_d] and python_player.x + VEL < WIDTH - 50: # !! THIS 50 REPRESENTS THE PLAYER WIDTH
            python_player.x += VEL
        if keys_pressed[pygame.K_w] and python_player.y <= 200:
             python_player.y -= 5

def java_player_movement(keys_pressed, java_player):
        if keys_pressed[pygame.K_LEFT] and java_player.x - VEL > 0:
            java_player.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and java_player.x + VEL < WIDTH - 50:
            java_player.x += VEL

def gravity(grav, player):
    if player.y < 200:
        player.y += grav


def main():
    python_player = pygame.Rect(200, 200, 50, 50)
    java_player = pygame.Rect(500, 200, 50, 50)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        python_player_movement(keys_pressed, python_player)
        java_player_movement(keys_pressed, java_player)
        gravity(GRAVITY, python_player)
        gravity(GRAVITY, java_player)

        draw_window(python_player, java_player)

    pygame.quit()

if __name__ == "__main__":
    main()