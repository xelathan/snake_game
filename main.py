import pygame 
from pygame.locals import *
import time

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('./resources/apple.jpeg').convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('./resources/block.jpeg').convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110, 110, 6))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        walkValue = 40

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= walkValue
        if self.direction == 'down':
            self.y[0] += walkValue
        if self.direction == 'left':
            self.x[0] -= walkValue
        if self.direction == 'right':
            self.x[0] += walkValue
        self.draw()

class Game: 
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 6))

        self.snake = Snake(self.surface, 6)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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
                
            self.play()
            time.sleep(0.3)
            

       
        

if __name__ == "__main__":
    game = Game()
    game.run()

    

    
    

    