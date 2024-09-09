import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    game_time = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill((0, 0, 0))
        drawable.draw(screen)
        dt = game_time.tick(60) / 1000
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
