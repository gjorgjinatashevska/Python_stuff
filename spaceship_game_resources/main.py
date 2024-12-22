import pygame
import random
import sys

pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# zvuci /mnt/data/clash_sound.wav
BACKGROUND_MUSIC = 'background_music.mp3'
CLASH_SOUND = 'class_sounds.mp3'
pygame.mixer.music.load('background_music.wav')
clash_sound = pygame.mixer.Sound('clash_sound.wav')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Scavenger")
clock = pygame.time.Clock()


player_img = pygame.image.load('spaceship.png')
player_rect = player_img.get_rect()
player_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
player_speed = 5

asteroid_img = pygame.image.load('asteroid.png')
asteroids = []
ASTEROID_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ASTEROID_EVENT, 1000)
crystal_img = pygame.image.load('energy_crystal.png')
crystals = []
CRYSTAL_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(CRYSTAL_EVENT, 3000)

score = 0
font = pygame.font.Font(None, 36)
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ASTEROID_EVENT:
            asteroid_rect = asteroid_img.get_rect()
            asteroid_rect.x = random.randint(0, WINDOW_WIDTH - asteroid_rect.width)
            asteroid_rect.y = -asteroid_rect.height
            asteroids.append(asteroid_rect)
        elif event.type == CRYSTAL_EVENT:
            crystal_rect = crystal_img.get_rect()
            crystal_rect.x = random.randint(0, WINDOW_WIDTH - crystal_rect.width)
            crystal_rect.y = -crystal_rect.height
            crystals.append(crystal_rect)

    # inputot
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_speed

    for asteroid in asteroids[:]:
        asteroid.y += 5
        if asteroid.colliderect(player_rect):
            clash_sound.play()
            running = False
        if asteroid.top > WINDOW_HEIGHT:
            asteroids.remove(asteroid)
    for crystal in crystals[:]:
        crystal.y += 3
        if crystal.colliderect(player_rect):
            score += 10
            crystals.remove(crystal)
        elif crystal.top > WINDOW_HEIGHT:
            crystals.remove(crystal)

    screen.blit(player_img, player_rect)

    for asteroid in asteroids:
        screen.blit(asteroid_img, asteroid)

    for crystal in crystals:
        screen.blit(crystal_img, crystal)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
