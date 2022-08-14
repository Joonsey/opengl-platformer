import pyglet
import random
from settings import *



class Movement_Particle(pyglet.shapes.Rectangle):
    def __init__(self,direction, x, y, color=..., batch=None):
        width = random.randrange(2,8)
        height = random.randrange(2,8)
        self.lifetime = random.randint(0,10) / 20
        self.velocity = random.randint(16,48)
        self.direction = direction
        color = (random.randint(150,255),255,255)

        if self.direction < 0:
            x += tile_size - width
        super().__init__(x, y, width, height, color, batch)


    def update(self, dt):

        if self.direction > 0:
            self.x += -self.velocity * dt
        else:
            self.x -= -self.velocity * dt
        self.y += self.velocity * dt

    def is_dead(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            return True
