import pyglet
from pyglet import resource
from entity import Friendly

from player import Player
from settings import *
from tile import Tile
from sprite_group import TileGroup, EntityGroup

class Level:
    def __init__(self, xdim, ydim,**kwargs) -> None:
        self.xdim = len(map_seed[0])
        self.ydim = len(map_seed)

        self.tiles_sprite_batch = pyglet.graphics.Batch()
        self.collision_tiles = TileGroup()
        self.entities = EntityGroup()
        self.entity_sprite_batch = pyglet.graphics.Batch()
        self.generate_tilemap()

    def generate_tilemap(self):
        tile = None # this gets caught later if unchanged
        for x in range(self.xdim):
            for y in range(self.ydim):
                kind = map_seed[y][x]
                xloc = x*tile_size
                yloc = (self.ydim*tile_size)-(y*tile_size)
                if kind == 69:
                    """
                    values between 0 -> 68 are tiles and static assets
                    69 is the player
                    70 -> ... is entities
                    """
                    self.player = Player(xloc, yloc, obstacles=self.collision_tiles)
                elif kind > 0 and kind < 69:
                    if kind == 1:
                        tile = Tile(kind, xloc, yloc, self.tiles_sprite_batch)
                        self.collision_tiles.append(tile)
                    else:
                        tile = Tile(kind, xloc, yloc, self.tiles_sprite_batch)
                    assert(tile != None)

                elif kind >= 70:
                    if kind == 71:
                        entity = Friendly(kind, xloc, yloc, batch=self.entity_sprite_batch)
                        self.entities.append(entity)

        self.player.obstacles = self.collision_tiles
        self.player.entities = self.entities


    def draw(self):
        self.tiles_sprite_batch.draw()
        self.entity_sprite_batch.draw()

