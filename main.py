import pygame 
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (98, 169, 67)

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
        self.render_background(self.parent_screen)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        #increase length of snake and append values into array
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def render_background(self, parent_screen):
        bg = pygame.image.load('./resources/background.jpeg')
        parent_screen.blit(bg, (0,0))

    
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
        pygame.mixer.init()
        self.play_background_music()
        self.GAME_SPEED = 0.3

        self.surface = pygame.display.set_mode((1000, 800))
        self.render_background()

        #Init snake object
        self.snake = Snake(self.surface, 1)
        self.snake.draw()

        #Init Apple object
        self.apple = Apple(self.surface)
        self.apple.draw()

    #collision check based on parameters of snake head and apple (snake with apple)
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play_background_music(self):
        pygame.mixer.music.load('./resources/bg_music_1.mp3')
        pygame.mixer.music.play()
    
    def play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load('./resources/background.jpeg')
        self.surface.blit(bg, (0,0))

    def speed_up_game(self):
        if self.GAME_SPEED > 0.03:
            self.GAME_SPEED -= 0.03


    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #collision check when snake head hits apple
        if(self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y)):
            self.play_sound('./resources/1_snake_game_resources_ding.mp3')
            self.speed_up_game()
            self.snake.increase_length()
            self.apple.move()
        
        #check to see if snake collides with its body blocks(itself)
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('./resources/1_snake_game_resources_crash.mp3')
                raise 'Game Over'

        if self.snake.x[0] < 0 or self.snake.x[0] > 1000 or self.snake.y[0] < 0 or self.snake.y[0] > 800:
            self.play_sound('./resources/1_snake_game_resources_crash.mp3')
            raise 'Game Over'
    
                

    #create UI for score and place it in
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))


    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press enter. To exit press escape", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset_game(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        pygame.mixer.music.unpause()

    def run(self):
        pause = False
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #Escape which closes window
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    if event.key == K_RETURN:
                        if pause:
                            pause = False
                            self.reset_game()


                    #Movement Key Input
                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True

            time.sleep(self.GAME_SPEED)
            

       
        
#Entry
if __name__ == "__main__":
    game = Game()
    game.run()

    

    
    

    