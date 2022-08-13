import pyglet
from settings import *

class Entity(pyglet.sprite.Sprite):
    def __init__(self, imgs, x=0, y=0):
        self.imgs = imgs
        self.idle_animation = pyglet.image.Animation.from_image_sequence(self.imgs, duration=1, loop=True)
        super().__init__(self.idle_animation, x, y)



class Friendly(Entity):
    def __init__(self, id, x=0, y=0):
        self.imgs = [
        pyglet.image.load('assets/characters/red-hooded-guy-0.png'),
        pyglet.image.load('assets/characters/red-hooded-guy-1.png')]
        super().__init__(self.imgs, x, y)

        self.interactable = False

    def interact(self):
        pass

    def draw(self):
        if self.interactable:
            self.color = (199,233,233)
        else:
            self.color = (255,255,255)
        return super().draw()


