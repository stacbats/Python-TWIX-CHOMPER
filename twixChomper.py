#  Pygame & Python
#  Udemey course on learning Pygame

import pygame, random
 
# initialse pygame
pygame.init()

# set our display surface
WINDOW_WIDTH = 950
WINDOW_HEIGHT = 420
display_surface = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Twix Chomper")

#   set up the fps and time
FPS = 60
clock = pygame.time.Clock()

#   set up the game values
PLAYER_STARTING_LIVES = 3
PLAYER_VELOCITY = 5
TWIX_STARTING_V = 5
TWIX_ACCELERATION = .5   #.5 increase move every 2 times 1 is every time
BUFFER_DISTANCE = 90

score = 0
player_lives = PLAYER_STARTING_LIVES
twix_velocity =TWIX_STARTING_V


#   set up colours
YELLOW =(255,255,0)
RED = ( 255,0,0)
MAROON = (129,0,0)
OLIVE =(128,128,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#   set display writing font
font = pygame.font.Font('BAUHS93.ttf', 32)

#   set up text
score_text = font.render("Score: " + str(score), True, RED,OLIVE)
score_rect = score_text.get_rect()
score_rect.topright = (240,20)

title_text = font.render("  TwiX chomPer  ",True ,YELLOW, MAROON)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH //2
title_rect.y = 10

lives_text = font.render("Lives: " +str(player_lives),True, RED,OLIVE)
lives_rect = lives_text.get_rect()
lives_rect.topleft = (WINDOW_WIDTH - 240,20)

game_over_txt = font.render("GAME OVER", True, YELLOW, OLIVE)
game_over_rect = game_over_txt.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_txt = font.render("Press Any Key to Continue", True, YELLOW, OLIVE)
continue_rect = continue_txt.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#   set up the sound
twix_sound = pygame.mixer.Sound("POP.wav")
miss_sound = pygame.mixer.Sound("Trump.wav")
# miss_sound.set_volume(.1)  Remove tag if want to decrease sound
pygame.mixer.music.load("OL2.mp3")
#pygame.mixer.music.load.set_volume(.1)
#   set up the images
player_image = pygame.image.load("TwixDemon.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2


twix_image = pygame.image.load("twix2.png")
twix_rect = twix_image.get_rect()
twix_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
twix_rect.y = random.randint (64,WINDOW_HEIGHT -32)

# main game loop
pygame.mixer.music.play(-1,0.0) #0.0
running = True
while running:
    #checking if game playing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    # checking to see if movement made
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    # move the twix's
    if twix_rect.x < 0:          # player misses coin
        player_lives -= 1
        miss_sound.play()
        twix_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        twix_rect.y = random.randint(64, WINDOW_HEIGHT-32)
    else:
        # move the twix
        twix_rect.x -= twix_velocity


    # collision detection etc.
    if player_rect.colliderect(twix_rect):
        score += 1
        twix_sound.play()
        twix_velocity += TWIX_ACCELERATION
        twix_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        twix_rect.y = random.randint(64, WINDOW_HEIGHT-32)

    # update scores etc.
    score_text = font.render("Score: " +str(score),True,  RED,OLIVE )
    lives_text = font.render("Lives: " +str(player_lives),True,  RED,OLIVE )

    # player lives
    if player_lives == 0:
        display_surface.blit(game_over_txt, game_over_rect)
        display_surface.blit(continue_txt, continue_rect)
        pygame.display.update()

        # pause game until player says yes
        pygame.mixer_music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    twix_velocity = TWIX_STARTING_V
                    pygame.mixer.music.play(-1,0,0)
                    is_paused= False
                # quit game
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False



    # fill the display
    display_surface.fill(BLACK)

    # Put Hd to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line (display_surface, WHITE, (0,64), (WINDOW_WIDTH,64),2)

    # put assets on screen
    display_surface.blit (twix_image, twix_rect)
    display_surface.blit (player_image, player_rect)    
    # update clock
    pygame.display.update()
    clock.tick(FPS)

    # end the game
pygame.quit()