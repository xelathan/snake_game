import pygame 
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('./resources/block.jpeg').convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 6))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
    
    def move_up(self):
        self.y -= 10
        self.draw()
    
    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

class Game: 
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((110, 110, 6))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #Escape which closes window
                    if event.key == K_ESCAPE:
                        pygame.quit()

                    #Movement Key Input
                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()
                #X which closes window
                elif event.type == QUIT:
                    pygame.quit()
            pass
       
        

if __name__ == "__main__":
    game = Game()
    game.run()

    

    
    

    