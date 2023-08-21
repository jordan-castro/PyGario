import math


class CollisionObserver:
    colliders = []

    # This allows us to pass in a List to the colliders list.
    def __unpack_coliders(self, colliders):
        cls = []
        for collider in colliders:
            if type(collider) in [list, tuple]:
                cls.extend(collider)
            else:
                cls.append(collider)
        self.colliders = cls

    def observe(self, player):
        for cl in self.colliders:
            if self.is_colliding(player, cl):
                player.collide(cl)
                cl.collide(player)

    def is_colliding(self, object_1, object_2):
        x1, y1 = object_1.position
        x2, y2 = object_2.position
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distance <= (object_1.radius):
            return True
        else:
            return False
        
    def set_colliders(self, colliders):
        self.__unpack_coliders(colliders)