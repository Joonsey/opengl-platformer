import pyglet
from pyglet.window import key

from level import Level
from player import Player
from settings import *


class Game(pyglet.window.Window):

    def __init__(self):
        super(Game, self).__init__()

        self.set_vsync(True)

        self.set_size(WIDTH, HEIGHT)
        self.keyboard = key.KeyStateHandler()
        self.push_handlers(self.keyboard)
        self.debug = pyglet.text.Label("video game", x=WIDTH-200, y=HEIGHT-20) # DEBUG THING
        self.fps_display = pyglet.window.FPSDisplay(window=self)

        pyglet.clock.schedule_interval(self.draw, 1/FPS)
        self.level = Level(11,11)


    def draw(self, dt):
        self.clear()
        self.fps_display.draw()
        self.debug.text = "x: " + str(int(self.level.player.momentum.x)) + ", y: " + str(int(self.level.player.momentum.y))
        self.debug.draw()
        self.level.draw()
        self.level.player.draw(self.keyboard, dt)


    def on_key_press(self, symbol, modifiers):
        pass
    def on_key_release(self, symbol, modifiers):
        pass

if __name__ == "__main__":
    game = Game()
    pyglet.app.run()
