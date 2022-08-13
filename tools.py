from PIL import Image
from settings import *
import os



def parse_h_tileset(image_path: str) -> None:
    file, ext = os.path.splitext(image_path)
    with Image.open(image_path) as im:
        i = im.width // tile_size
        for index in range(i):
            x_offset = index*tile_size
            _im = im.crop((x_offset,0, x_offset + tile_size, tile_size))
            print(_im.width)
            _file_name = file+'-'+str(index)+ext
            _im.save(_file_name, 'png')
            print('image saved as: ' + _file_name)


def parse_v_tileset(image_path: str) -> None:
    file, ext = os.path.splitext(image_path)
    with Image.open(image_path) as im:
        i = im.height // tile_size
        for index in range(i):
            y_offset = index*tile_size
            _im = im.crop((0,y_offset ,tile_size, y_offset+tile_size))
            _file_name = file+'-'+str(index)+ext
            _im.save(_file_name, 'png')

if __name__ == "__main__":
    img ='assets/characters/red-hooded-guy.png'
    parse_h_tileset(img)
    parse_v_tileset(img)

