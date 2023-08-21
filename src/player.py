import pygame as pg
import food


# Player
class Player(food.Food):
    to_grow = 0

    def __init__(self, screen, color) -> None:
        super().__init__(screen, color)
        self.speed = 0.5
        self.radius = 20 # Player start radius

    def draw(self):
        if self.to_grow > 0:
            self.grow()
        return super().draw()

    def collide(self, collider: food.Food):
        self.to_grow = collider.radius

    def grow(self):
        self.radius += (self.to_grow - (self.to_grow - 1))
        self.to_grow = self.to_grow - 1
        print(self.radius)
        print(self.to_grow)

    def move(self, keys):
        if keys[pg.K_LEFT]:
            self.position[0] -= self.speed
        if keys[pg.K_RIGHT]:
            self.position[0] += self.speed
        if keys[pg.K_UP]:
            self.position[1] -= self.speed
        if keys[pg.K_DOWN]:
            self.position[1] += self.speed
