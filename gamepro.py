import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Epic Platformer Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Frames per second
FPS = 60
clock = pygame.time.Clock()

# Player settings
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_COLOR = BLUE

# Gravity and Jump Settings
GRAVITY = 1
JUMP_STRENGTH = -20

# Platform settings
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = GREEN

# Font
font = pygame.font.SysFont(None, 55)

# Load background image
bg = pygame.image.load('background.jpg').convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Check for collision with ground
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH


# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=PLATFORM_WIDTH, height=PLATFORM_HEIGHT):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Generate random platforms
def generate_platforms(num_platforms):
    platforms = pygame.sprite.Group()
    for i in range(num_platforms):
        x = random.randint(0, WIDTH - PLATFORM_WIDTH)
        y = random.randint(100, HEIGHT - PLATFORM_HEIGHT)
        platform = Platform(x, y)
        platforms.add(platform)
    return platforms


# Check for collision between player and platforms
def check_collision(player, platforms):
    collisions = pygame.sprite.spritecollide(player, platforms, False)
    if collisions and player.velocity_y > 0:
        player.rect.bottom = collisions[0].rect.top
        player.velocity_y = 0
        player.on_ground = True


# Main game loop
def game():
    running = True
    score = 0

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    platforms = generate_platforms(10)
    all_sprites.add(platforms)

    # Main loop
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Update
        all_sprites.update()
        check_collision(player, platforms)

        # Draw
        screen.fill(WHITE)
        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, [10, 10])

        # Update screen
        pygame.display.flip()

    pygame.quit()


# Start the game
if __name__ == '__main__':
    game()
