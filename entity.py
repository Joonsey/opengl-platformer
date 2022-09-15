import pyglet
from pyglet import resource

from settings import *

class Entity(pyglet.sprite.Sprite):
    def __init__(self, imgs, x=0, y=0, batch=None):
        self.imgs = imgs
        self.idle_animation = pyglet.image.Animation.from_image_sequence(self.imgs, duration=1, loop=True)
        super().__init__(self.idle_animation, x, y, batch=batch)



class Friendly(Entity):
    def __init__(self, id, x=0, y=0, batch=None):
        self.imgs = [
        resource.image('assets/characters/red-hooded-guy-0.png'),
        resource.image('assets/characters/red-hooded-guy-1.png')]
        super().__init__(self.imgs, x, y, batch=batch)

        self.interactable = False

    def interact(self):
        """
        #interact with entity:
        - trigger dialoge
        - event
        - etc
        """
        pass

    def can_interact(self):
        if not self.interactable:
            self.opacity = 128

    def can_no_longer_interact(self):
        if self.interactable:
            self.opacity = 255




