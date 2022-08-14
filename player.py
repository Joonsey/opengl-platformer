import pyglet
from pyglet.window import key

from entity import Friendly
from tile import Tile
from button import Button
from sprite_group import *
from settings import *


class Player:
    def __init__(self, xpos: int, ypos: int, obstacles: TileGroup) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.texture = pyglet.image.load('texture.png')
        self.momentum = pyglet.math.Vec2(0,0)
        self.speed = 320.0
        self.max_speed = self.speed
        self.jumpspeed = 64.0*6
        self.on_ground = True
        self.gravity = 600

        self.sprite = pyglet.sprite.Sprite(self.texture,
                                           self.xpos,
                                           self.ypos)
        self.obstacles = obstacles
        self.entities = []
        self.jumped = False
        self.interact_radius = 32

    def draw(self, keyboard, dt):
        self.interactable_object = self.get_interactable()
        self.movement_handler(keyboard, dt)
        self.sprite.draw()
        if self.button != None:
            self.button.draw()

    def movement_handler(self, keyboard, dt) -> None:

        # x movement resistance
        if self.momentum.x > 0:
            if self.momentum.x < self.speed * dt:
                self.momentum = pyglet.math.Vec2(0, self.momentum.y)
            else:
                self.momentum -= self.speed * dt, 0
        elif self.momentum.x < 0:
            if self.momentum.x > -self.speed * dt:
                self.momentum = pyglet.math.Vec2(0, self.momentum.y)
            else:
                self.momentum += self.speed * dt, 0

        # handling input
        if keyboard[key.D]:
            if self.momentum.x < self.max_speed:
                self.momentum += int(self.speed * (dt*4)), 0

        if keyboard[key.A]:
            if self.momentum.x > -self.max_speed:
                self.momentum -= int(self.speed * (dt*4)), 0

        if keyboard[key.SPACE] and not self.jumped:
            self.jumped = True
            self.momentum += 0, self.jumpspeed

        # calculating x movement and checking for collision
        self.sprite.x += self.momentum.x * dt
        colliding = self.collision()
        if colliding:
            if self.momentum.x >= 0:

                self.sprite.x = colliding.x - tile_size
            else:

                self.sprite.x = colliding.x + tile_size
            self.momentum = pyglet.math.Vec2(0, self.momentum.y)


        # calculating y movement and checking for collision
        self.momentum -= 0, self.gravity * dt
        self.sprite.y += self.momentum.y * dt
        colliding = self.collision()
        if colliding:
            if self.momentum.y <= 0:
                self.sprite.y = colliding.y + tile_size
                self.jumped = False
            else:
                self.sprite.y = colliding.y - tile_size
            self.momentum = pyglet.math.Vec2(self.momentum.x, 0)

        # handle exit game
        if keyboard[key.Q]:
            pyglet.app.exit()


        # player interacts with object
        if keyboard[key.E] and self.get_interactable():
            self.interact(self.interactable_object)

    def collision(self) -> Tile | None:
        for obstacle in self.obstacles:
            sprite = obstacle
            if self.sprite.x < sprite.x + sprite.width and self.sprite.x + self.sprite.width > sprite.x and self.sprite.y < sprite.y + sprite.height and self.sprite.y + self.sprite.height > sprite.y:

                # COLOR DEBUGING
                # this should be toggled off at some point, unless it's just cool pogchamp
                # could make it fade for some cool game mechanic at some point
                # pyglet.clock something to make a function that redrawst he color with cool fade
                # TODO fucking with this for fun
                obstacle.color = (255,0,0)
                obstacle._update_color()
                return obstacle


    def get_interactable(self) -> Friendly | None:
        for entity in self.entities:
            if type(entity) == Friendly:
                centerx = (entity.x + entity.width) // 2
                centery = (entity.y + entity.height) // 2
                _p_centerx = (self.sprite.x + self.sprite.width) // 2
                _p_centery = (self.sprite.y + self.sprite.height) // 2
                if abs(_p_centerx - centerx) < self.interact_radius and abs(_p_centery - centery) < self.interact_radius:
                    self.button = Button('e', self.sprite.x, self.sprite.y + tile_size)
                    entity.interactable = True
                    return entity
                else:
                    self.button = None
                    entity.interactable = False

    def interact(self, interactable_object: Friendly | None) -> None:
        if interactable_object == None:
            pass
        else:
            interactable_object.interact()

