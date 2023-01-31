import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Eye-Hand Coordination Game')

# Define the colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Initialize the clock
clock = pygame.time.Clock()

# Initialize the score
score = 0

# Define the Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Initialize the list of circles
circles = []

# Keep track of the number of red circles generated
total_circles = 0

# Keep track of the number of successful catches
successful_catches = 0

# Initialize the time limit in seconds
time_limit = 60

# Initialize the sound effect
sound = pygame.mixer.Sound('440.ogg')

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Generate a new circle randomly
    if len(circles) < 10:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        radius = 20
        color = red
        circles.append(Circle(x, y, radius, color))
        total_circles += 1

    # Draw the circles
    for circle in circles:
        circle.draw()

    # Check if the mouse click is inside a circle
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i, circle in enumerate(circles):
            if (mouse_x - circle.x) ** 2 + (mouse_y - circle.y) ** 2 < circle.radius ** 2:
                score += 10
                successful_catches += 1
                del circles[i]
                sound.play()
                break

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, white)
    screen.blit(text, (10, 10))

    # Display the accuracy
    accuracy = 100 * successful_catches / total_circles if total_circles != 0 else 0
    text = font.render(f'Accuracy: {accuracy:.2f}%', True, white)
    screen.blit(text, (10, 50))

    # Display the time limit and countdown
    time_left = time_limit - pygame.time.get_ticks() // 1000
    text = font.render(f'Time: {time_left}', True, white)
    screen.blit(text, (400, 10))

    # Check if the time limit has been reached
    if time_left <= 0:
        running = False

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()

# Show the final score
print(f'Final Score: {score}')

