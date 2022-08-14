import pyglet
import random

from settings import *

class Tile(pyglet.sprite.Sprite):

    def __init__(self, kind, x=0, y=0):
        self.ground_images = self.format_path('ground-', (1,6))
        self.grass_images = self.format_path('grass-', (0,4))
        self.barrel_images = self.format_path('barrel-', (1,2))


        self.img = pyglet.image.load(random.choice(self.ground_images))
        if kind == 1:
            self.img = self.select_random_image(self.ground_images)
        elif kind == 2:
            self.img = self.select_random_image(self.grass_images)
        elif kind == 3:
            self.img = self.select_random_image(self.barrel_images)
        elif kind == 4:
            self.imgs = [pyglet.image.load(x) for x in self.format_path('flower-', (0,9))]
            self.img = pyglet.image.Animation.from_image_sequence(self.imgs, duration=0.5, loop=True)
        elif kind == 5:
            self.img = pyglet.image.load(self.format_path("ladder-")[0])

        super().__init__(self.img, x, y)

    def select_random_image(self, img: list[str]):
        return pyglet.image.load(random.choice(img))

    def format_path(self, base_str: str, ranges:tuple | None = None) -> list[str]:
        if ranges:
            return [ASSET_PATH+base_str+str(x)+".png" for x in range(ranges[0], ranges[1])]
        else:
            return [ASSET_PATH+base_str+"0.png"]


