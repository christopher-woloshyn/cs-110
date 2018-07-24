import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self,hero,controller):
        """ updates the enemy object's position within the bounds of the screen.

            args: self [enemy] - the object that is being changed by this method.
                  hero [hero] - referenced by the moveTowardsPlayer() method.
                  controller [controller] - referenced by the enemy object to check if its position is within the bounds of the screen.

            return: None.
        """
        previous_x = self.rect.x
        previous_y = self.rect.y
        random_move = random.randrange(30) #creates a 1 in 30 chance the enemy will move towards the hero every frame.

        if not random_move:
            self.moveTowardsPlayer(hero)
        else:
            self.randomMove()

        if not(0 < self.rect.x < controller.width - 100) or not(0 < self.rect.y < controller.height - 100):
            self.rect.x = previous_x
            self.rect.y = previous_y

    def randomMove(self):
        """ randomly adds the enemy object's speed, subtracts the enemy object's speed or does nothing to the x and y coordinates.

            args: self [enemy] - the object that is being changed by this method.

            return: None.
        """
        self.rect.x += self.speed*random.randint(-1,1)
        self.rect.y += self.speed*random.randint(-1,1)

    def moveTowardsPlayer(self,hero):
        """ changes the enemy object's position in order to move closer to the hero object.

            args: self [enemy] - the object that is being changed by this method.
                  hero [hero] - referenced by the enemy object to determine which direction to move.

            return: None.
        """
        if hero.rect.x > self.rect.x:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if hero.rect.y > self.rect.y:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed


        
