import sys
import pygame
import random
from src import hero
from src import enemy

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """Load the sprites that we need"""
        self.enemies = pygame.sprite.Group()
        for i in range(3):
            x = random.randrange(100, self.width - 100)
            y = random.randrange(100, self.height - 100)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png' ))
        self.hero = hero.Hero("Conan", 50, 50, "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies))
        self.heart = pygame.image.load("assets/heart.png")

    def mainLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()
            #check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                    else:
                        self.enemies.add(e)
                        self.background.fill((250, 0, 0))

            if(self.hero.current_health == 0):
                self.hero.kill()
                self.update()
                sys.exit()

            #redraw the entire screen
            self.update()

    def update(self):
        """ updates the models, redraws the background, redraws the sprites, redraws the hero's health in hearts, and updates the display.

            args: self [controller] - the object that is being changed by this method.

            return: None.
        """
        self.enemies.update(self.hero,self)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.drawHearts(self.hero.current_health)
        pygame.display.flip()

    def drawHearts(self,number):
        """ draws an integer number of hearts representing the hero's health

            args: self [controller] - the object that is being changed by this method.
                  number [int] - the number of hearts to draw on the display.

            return: None.
        """
        for i in range(number):
            self.screen.blit(self.heart,((self.width - (30*self.hero.max_health) + (30*i),20)))
            #the hero.max_health attribute allows for this function to work even if the max health of the hero changes

def main():
    main_window = Controller()
    main_window.mainLoop()
main()
