import pyglet
from settings import *

class Button(pyglet.sprite.Sprite):
    def __init__(self, kind, x=0, y=0):
        self.imgs = [
        pyglet.image.load('assets/button/e-button-0.png'),
        pyglet.image.load('assets/button/e-button-1.png')
        ]
        self.idle_animation = pyglet.image.Animation.from_image_sequence(self.imgs, duration=1, loop=True)
        super().__init__(self.idle_animation, x, y)

