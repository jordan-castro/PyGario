import pygame as pg

# Initiate the pygame module
pg.init()

# Window
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Agario')

# Circle properties
circle_color = (255, 0, 0)  # Red color in RGB format
circle_center = (400, 300)  # (x, y) coordinates of the circle's center
circle_radius = 50

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the circle
    pg.draw.circle(screen, circle_color, circle_center, circle_radius)

    # Update the display
    pg.display.flip()

pg.quit()