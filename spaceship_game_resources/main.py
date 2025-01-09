import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BLACK = (0, 0, 8)
WHITE = (255, 255, 255)

# Sounds
BACKGROUND_MUSIC = 'background_music.wav'
CLASH_SOUND = 'clash_sound.wav'
pygame.mixer.music.load(BACKGROUND_MUSIC)
clash_sound = pygame.mixer.Sound(CLASH_SOUND)
pygame.mixer.music.play(-1)  # Loop background music

# Screen Setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Scavenger")
clock = pygame.time.Clock()

# Player Setup
player_img = pygame.image.load('spaceship.png')
player_img = pygame.transform.scale(player_img, (100, 100))  # Resize to smaller size

player_rect = player_img.get_rect()
player_rect.center = (WINDOW_WIDTH // 3, WINDOW_HEIGHT - 30)
player_speed = 5

# Asteroid Setup
asteroid_img = pygame.image.load('asteroid.png')
asteroid_img = pygame.transform.scale(asteroid_img, (100, 100))  # Resize to smaller size
asteroids = []
ASTEROID_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ASTEROID_EVENT, 1000)

# Crystal Setup
crystal_img = pygame.image.load('energy_crystal.png')
crystals = []
CRYSTAL_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(CRYSTAL_EVENT, 3000)

# Scoring
score = 0
font = pygame.font.Font(None, 36)

# Game Loop
running = True
while running:
    # Fill the background
    screen.fill(BLACK)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ASTEROID_EVENT:
            # Spawn a new asteroid
            asteroid_rect = asteroid_img.get_rect()
            asteroid_rect.x = random.randint(0, WINDOW_WIDTH - asteroid_rect.width)
            asteroid_rect.y = -asteroid_rect.height
            asteroids.append(asteroid_rect)
        elif event.type == CRYSTAL_EVENT:
            # Spawn a new crystal
            crystal_rect = crystal_img.get_rect()
            crystal_rect.x = random.randint(0, WINDOW_WIDTH - crystal_rect.width)
            crystal_rect.y = -crystal_rect.height
            crystals.append(crystal_rect)

    # Handle Player Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_speed

    # Update Asteroids
    for asteroid in asteroids[:]:
        asteroid.y += 5  # Move asteroid down
        if asteroid.colliderect(player_rect):
            # Play clash sound for feedback but don't stop the game
            clash_sound.play()
        if asteroid.top > WINDOW_HEIGHT:
            asteroids.remove(asteroid)

    # Update Crystals
    for crystal in crystals[:]:
        crystal.y += 3  # Move crystal down
        if crystal.colliderect(player_rect):
            score += 10  # Increase score
            crystals.remove(crystal)
        elif crystal.top > WINDOW_HEIGHT:
            crystals.remove(crystal)

    # Draw Player
    screen.blit(player_img, player_rect)

    # Draw Asteroids
    for asteroid in asteroids:
        screen.blit(asteroid_img, asteroid)

    # Draw Crystals
    for crystal in crystals:
        screen.blit(crystal_img, crystal)

    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update Display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
