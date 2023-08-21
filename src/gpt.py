import pygame
import random
import math

pygame.init()

# Create a Pygame window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Collision Example")

# Define circle properties
circle_radius_1 = 30
circle_radius_2 = 60
circle_x1 = random.randint(circle_radius_1, screen_width - circle_radius_1)
circle_y1 = random.randint(circle_radius_1, screen_height - circle_radius_1)
circle_x2 = random.randint(circle_radius_2, screen_width - circle_radius_2)
circle_y2 = random.randint(circle_radius_2, screen_height - circle_radius_2)
circle_color = (0, 255, 0)  # Green

# Calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the second circle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x2 -= 5
    if keys[pygame.K_RIGHT]:
        circle_x2 += 5
    if keys[pygame.K_UP]:
        circle_y2 -= 5
    if keys[pygame.K_DOWN]:
        circle_y2 += 5

    # Check for collision
    if distance(circle_x1, circle_y1, circle_x2, circle_y2) <= (circle_radius_2 * 2):
        circle_color = (255, 0, 0)  # Red for collision
    else:
        circle_color = (0, 255, 0)  # Green for no collision

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circles
    pygame.draw.circle(screen, circle_color, (circle_x1, circle_y1), circle_radius_2)
    pygame.draw.circle(screen, (0, 0, 255), (circle_x2, circle_y2), circle_radius_1)  # Blue for the second circle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
