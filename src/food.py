import pygame as pg
import random


class Food:
    def __init__(self, screen: pg.surface.Surface, color: tuple) -> None:
        # Args that are passed
        self.screen = screen
        self.color = color
        # Args that are set
        self.position = [0, 0]
        self.radius = 10  # Start radius
        self.show = True

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.position, self.radius)

    def collide(self, collider):
        # When collided
        if hasattr(collider, 'move'):
            # Is player, go away
            self.show = False
            self.radius = 0

    @staticmethod
    def random(screen):
        r_color = [random.randint(1, 255) for x in range(3)]
        r_pos = [
            random.randint(0, screen.get_width()),
            random.randint(0, screen.get_height()),
        ]
        f = Food(screen, r_color)
        f.position = r_pos
        return f
