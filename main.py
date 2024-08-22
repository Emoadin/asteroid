import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)  
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))  # this had to come after Player.containers so that it knows about the groups

    

    dt = 0
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        #player.draw(screen)
        
        #player.update(dt)
        screen.fill((0,0,0))
        

        

        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if player.collision(obj):
                print("GAME OVER!!!")                
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()


        pygame.display.flip()
        

        dt = clock.tick(60) / 1000

    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")





if __name__ == "__main__":
    main()