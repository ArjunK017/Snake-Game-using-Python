import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# the Snake class
class Snake:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.size = 10
        self.speed = 10
        self.direction = 'right'   
        self.body = [(self.x, self.y)]
    
    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        
        self.body.insert(0, (self.x, self.y))
        self.body.pop()
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, black, (x, y, self.size, self.size))

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, window_width - 10)
        self.y = random.randint(0, window_height - 10)
        self.size = 10
    
    def draw(self):
        pygame.draw.rect(window, red, (self.x, self.y, self.size, self.size))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Main game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
            elif event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
    
    # Move the Snake
    snake.move()
    
    # Check for collision with the Food
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        food = Food()
        snake.body.append(snake.body[-1])
    
    # Check for collision with the walls
    if snake.x < 0 or snake.x > window_width - snake.size or snake.y < 0 or snake.y > window_height - snake.size:
        game_over = True
    
    # Check for collision with the Snake's body
    for i in range(1, len(snake.body)):
        if snake.body[0][0] == snake.body[i][0] and snake.body[0][1] == snake.body[i][1]:
            game_over = True
    
    # Draw the game objects
    window.fill(white)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Set the game clock
    clock.tick(10)

# Quit Pygame
pygame.quit()