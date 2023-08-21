import pygame as pg

from food import Food
from player import Player
from collision_observer import CollisionObserver

# Initiate the pygame module
pg.init()

# Window
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Agario")

# <-- Objects -->
player = Player(screen, (255, 255, 255))
foods = [Food.random(screen) for x in range(10)]

# <-- Observers -->
cls_obs = CollisionObserver()
cls_obs.set_colliders(foods)

running = True
while running:
    print("running")
    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Check to draw food
    for food in foods:
        if food.show:
            food.draw()
        else:
            foods.remove(food)
    
    player.move(pg.key.get_pressed())
    player.draw()

    cls_obs.observe(player)

    # Update the display
    pg.display.flip()

pg.quit()
