import pygame
from constants import *
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # Then create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all sprites
        updatable.update(dt)
        
        # Clear the screen
        screen.fill("black")
        
        # Draw all sprites
        for entity in drawable:
            entity.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

