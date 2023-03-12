"""
Adam's 2023 "Hackathon" Project
2023-03-10
"""

import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python vs Java")

HURT_SOUND = pygame.mixer.Sound(os.path.join("data", "hurt_sound.wav"))
BLOCK_SOUND = pygame.mixer.Sound(os.path.join("data", "block_sound.wav"))
PYTHON_PUNCH_SOUND = pygame.mixer.Sound(os.path.join("data", "python_punch.wav"))
PYTHON_KICK_SOUND = pygame.mixer.Sound(os.path.join("data", "python_kick.wav"))

MUSIC = pygame.mixer.music.load(os.path.join("data", "Python_vs_Java_Theme.wav"))

FPS = 60
VEL = 5

PYTHON_CHAR_IMAGE = pygame.image.load(os.path.join("data", "python_sprite.png"))
PYTHON_CHAR = pygame.transform.scale(PYTHON_CHAR_IMAGE, (250, 212))
PYTHON_PUNCH_IMAGE = pygame.image.load(os.path.join("data", "python_sprite_punch.png"))
PYTHON_PUNCH = pygame.transform.scale(PYTHON_PUNCH_IMAGE, (333, 212))
PYTHON_KICK_IMAGE = pygame.image.load(os.path.join("data", "python_sprite_kick.png"))
PYTHON_KICK = pygame.transform.scale(PYTHON_KICK_IMAGE, (250, 212))
PYTHON_BLOCK_IMAGE = pygame.image.load(os.path.join("data", "python_sprite_block.png"))
PYTHON_BLOCK = pygame.transform.scale(PYTHON_BLOCK_IMAGE, (250, 212))

JAVA_CHAR_IMAGE = pygame.image.load(os.path.join("data", "java_sprite.png"))
JAVA_CHAR = pygame.transform.scale(JAVA_CHAR_IMAGE, (250, 212))
JAVA_PUNCH_IMAGE = pygame.image.load(os.path.join("data", "java_sprite_punch.png"))
JAVA_PUNCH = pygame.transform.scale(JAVA_PUNCH_IMAGE, (333, 212))
JAVA_KICK_IMAGE = pygame.image.load(os.path.join("data", "java_sprite_kick.png"))
JAVA_KICK = pygame.transform.scale(JAVA_KICK_IMAGE, (333, 212))
JAVA_BLOCK_IMAGE = pygame.image.load(os.path.join("data", "java_sprite_block.png"))
JAVA_BLOCK = pygame.transform.scale(JAVA_BLOCK_IMAGE, (250, 212))

PYTHON_CHAR_HIT = pygame.USEREVENT + 1
JAVA_CHAR_HIT = pygame.USEREVENT + 2

BG = pygame.image.load(os.path.join("data", "PvJ_BG.png"))

FONT = pygame.font.SysFont('impact', 40)

def draw_window(python_player, java_player, python_player_health, java_player_health, python_current_sprite, java_current_sprite):
    """
    Draw on surface

    Draws images/text to surface (screen)

    :param python_player: A pygame rect object
    :param java_player: A pygame rect object
    :param python_player_health: An int
    :param java_player_health: An int
    :param python_current_sprite: A list
    :param java_current_sprite: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Draws arguments to screen
    """
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(0, 0, 160, 50))
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(WIDTH - 160, 0, 160, 50))
    python_player_health_text = FONT.render("Health: " + str(python_player_health), 1, (255, 0, 0))
    java_player_health_text = FONT.render("Health: " + str(java_player_health), 1, (255, 0, 0))
    WIN.blit(python_player_health_text, (0, 0))
    WIN.blit(java_player_health_text, (WIDTH - java_player_health_text.get_width(), 0))

    WIN.blit(java_current_sprite[0], (java_player.x, java_player.y))
    WIN.blit(python_current_sprite[0], (python_player.x, python_player.y))

    pygame.display.update()

def python_player_movement(keys_pressed, python_player, java_player, block_state):
    """
    Move python

    :param keys_pressed: A pygame event key object
    :param python_player: A pygame rect object
    :param java_player: A pygame rect object
    :param block_state: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Moves python in given x direction
    """
    if keys_pressed[pygame.K_a] and python_player.x - VEL > 0:
        if block_state[0] == 'False':
            python_player.x -= VEL
    if keys_pressed[pygame.K_d] and python_player.x + VEL < WIDTH - 250 and python_player.x + 200 < java_player.x: # !! THIS 250 REPRESENTS THE PLAYER WIDTH
        if block_state[0] == 'False':
            python_player.x += VEL

def java_player_movement(keys_pressed, java_player, python_player, block_state):
    """
    Move java

    :param keys_pressed: A pygame event key object
    :param java_player: A pygame rect object
    :param python_player: A pygame rect object
    :param block_state: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Moves java in given x direction
    """
    if keys_pressed[pygame.K_LEFT] and java_player.x - VEL > 0 and java_player.x > python_player.x + 200:
        if block_state[0] == 'False':
            java_player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and java_player.x + VEL < WIDTH - 250:
        if block_state[0] == 'False':
            java_player.x += VEL

def punch(puncher, punched, is_blocking):
    """
    Punch attack

    :param puncher: A pygame rect object
    :param punched: A pygame rect object
    :param is_blocking: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Performs punch attack
    """
    if puncher.colliderect(punched):
        if is_blocking[0] == 'True':
            BLOCK_SOUND.play()
            knockback(punched, puncher)
        else:            
            if puncher.x < punched.x:
                pygame.event.post(pygame.event.Event(JAVA_CHAR_HIT))
            else:
                pygame.event.post(pygame.event.Event(PYTHON_CHAR_HIT))
            knockback(puncher, punched)    

def kick(kicker, kicked, is_blocking):
    """
    Kick attack

    :param kicker: A pygame rect object
    :param kicked: A pygame rect object
    :param is_blocking: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Performs kick attack
    """
    if kicker.colliderect(kicked):
        if is_blocking[0] == 'True':
            BLOCK_SOUND.play()
            knockback(kicked, kicker)
        else:
            if kicker.x < kicked.x:
                pygame.event.post(pygame.event.Event(JAVA_CHAR_HIT))
            else:
                pygame.event.post(pygame.event.Event(PYTHON_CHAR_HIT))
            knockback(kicker, kicked)

def python_block(keys_pressed, python_block_state, python_current_sprite):
    """
    Python defensive block

    :param keys_pressed: A pygame event key object
    :param python_block_state: A list
    :param python_current_sprite: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Performs defensive block
    """
    if keys_pressed[pygame.K_b]:
        python_current_sprite[0] = PYTHON_BLOCK
        python_block_state[0] = 'True'

def java_block(keys_pressed, java_block_state, java_current_sprite):
    """
    Java defensive block

    :param keys_pressed: A pygame event key object
    :param java_block_state: A list
    :param java_current_sprite: A list
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Performs defensive block
    """
    if keys_pressed[pygame.K_PERIOD]:
        java_current_sprite[0] = JAVA_BLOCK
        java_block_state[0] = 'True'

def python_unblock(python_block_state):
    """
    Python unblock

    :param python_block_state: A list
    :precondition: Argument must be its respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Change to unblock state
    """
    if python_block_state[0] == 'True':
        python_block_state[0] = 'False'

def java_unblock(java_block_state):
    """
    Java unblock

    :param java_block_state: A list
    :precondition: Argument must be its respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Change to unblock state
    """
    if java_block_state[0] == 'True':
        java_block_state[0] = 'False'

def knockback(knocker, knocked):
    """
    Apply knockback

    :param knocker: A pygame rect object
    :param knocked: A pygame rect Object
    :precondition: All arguments must be their respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Applies knockback to knocked
    """
    if knocked.x + VEL < WIDTH - 250 and knocked.x - VEL > 0:
        if knocker.x < knocked.x:
            knocked.x += 25
        else:
            knocked.x -= 25

def winner(text):
    """
    Set/display winner text

    :param text: A string
    :precondition: Argument must be its respective data type, in relation with pygame documentation and PvJ standards.
    :postcondition: Displays winner text on the screen
    """
    winner_text = FONT.render(text, 1, (255, 0, 0))
    WIN.blit(winner_text, (WIDTH / 2 - winner_text.get_width() / 2, HEIGHT / 2 - winner_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    """
    Drives the program
    """
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    python_player = pygame.Rect(200, 250, 250, 212)
    java_player = pygame.Rect(500, 250, 250, 212)

    python_current_sprite = [PYTHON_CHAR]
    java_current_sprite = [JAVA_CHAR]

    python_player_health = 15
    java_player_health = 15

    python_player_blocking = ['False']
    java_player_blocking = ['False']

    python_player_cd = 0
    java_player_cd = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if pygame.time.get_ticks() - python_player_cd >= 1000:
                        python_current_sprite[0] = PYTHON_PUNCH
                        if python_player_blocking[0] == 'False':
                            PYTHON_PUNCH_SOUND.play()
                            punch(python_player, java_player, java_player_blocking)
                            python_player_cd = pygame.time.get_ticks()
                else:
                    python_current_sprite[0] = PYTHON_CHAR
                if event.key == pygame.K_m:
                    if pygame.time.get_ticks() - java_player_cd >= 1000:
                        java_current_sprite[0] = JAVA_PUNCH
                        if java_player_blocking[0] == 'False':
                            punch(java_player, python_player, python_player_blocking)
                            java_player_cd = pygame.time.get_ticks()
                else:
                    java_current_sprite[0] = JAVA_CHAR

                if event.key == pygame.K_v:
                    if pygame.time.get_ticks() - python_player_cd >= 1000:
                        python_current_sprite[0] = PYTHON_KICK
                        if python_player_blocking[0] == 'False':
                            PYTHON_KICK_SOUND.play()
                            kick(python_player, java_player, java_player_blocking)
                            python_player_cd = pygame.time.get_ticks()
                if event.key == pygame.K_COMMA:
                    if pygame.time.get_ticks() - java_player_cd >= 1000:
                        java_current_sprite[0] = JAVA_KICK
                        if java_player_blocking[0] == 'False':
                            kick(java_player, python_player, python_player_blocking)
                            java_player_cd = pygame.time.get_ticks()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                    python_current_sprite[0] = PYTHON_CHAR
                    python_unblock(python_player_blocking)
                if event.key == pygame.K_PERIOD:
                    java_current_sprite[0] = JAVA_CHAR
                    java_unblock(java_player_blocking)

            if event.type == PYTHON_CHAR_HIT:
                python_player_health -= 1
                HURT_SOUND.play()

            if event.type == JAVA_CHAR_HIT:
                java_player_health -=1
                HURT_SOUND.play()

        winner_text = ""
        if python_player_health <= 0:
            winner_text = "JAVA WINS!"
        if java_player_health <= 0:
            winner_text = "PYTHON WINS!"
        if winner_text != "":
            winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        python_player_movement(keys_pressed, python_player, java_player, python_player_blocking)
        java_player_movement(keys_pressed, java_player, python_player, java_player_blocking)

        python_block(keys_pressed, python_player_blocking, python_current_sprite)
        java_block(keys_pressed, java_player_blocking, java_current_sprite)

        draw_window(python_player, java_player, python_player_health, java_player_health, python_current_sprite, java_current_sprite)

    pygame.quit()

if __name__ == "__main__":
    main()