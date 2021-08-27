import pygame 
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('./resources/apple.jpeg').convert()
        self.parent_screen = parent_screen
        self.x = random.randint(2, 24) * SIZE
        self.y = random.randint(2, 19) * SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    #move apple position to random place on screen
    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE



class Snake:
    def __init__(self, parent_screen, length):
        #Init length, parent_screen, image-block, number of x/y blocks, direction
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('./resources/block.jpeg').convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        #wipe screen and recolor with each block and its coordinates
        self.parent_screen.fill((110, 110, 6))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        #increase length of snake and append values into array
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    
    #set direction based on keycode
    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):

        #the other blocks new position becomes the position of the block that was ahead of it
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        #head of snake moves by increment and its new position is set to that
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()

class Game: 
    def __init__(self):
        #Init pygame and create/color window
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 6))

        #Init snake object
        self.snake = Snake(self.surface, 1)
        self.snake.draw()

        #Init Apple object
        self.apple = Apple(self.surface)
        self.apple.draw()

    #collision check based on parameters of snake head and apple
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #collision check when snake head hits apple
        if(self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y)):
            self.snake.increase_length()
            self.apple.move()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

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
            

       
        
#Entry
if __name__ == "__main__":
    game = Game()
    game.run()

    

    
    

    