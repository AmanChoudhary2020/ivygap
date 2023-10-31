import numpy as np
from typing import Iterable

'''

tile size: 2x2

x x x 
x x x
x x x 
x x x 
'''

def coordinate_generator(image_size: tuple[int, int], tile_size: tuple[int, int], slide_x: int, slide_y: int) -> Iterable[tuple[int, int]]:
    image_width, image_height = image_size
    tile_width, tile_height = tile_size

    for y in range(0, image_height - tile_height + 1, slide_y):
        for x in range(0, image_width - tile_width + 1, slide_x):
            yield (x, y)

def tile_generator(image, tile_size, coordinates):
    tile_width, tile_height = tile_size
    image_width, image_height = image.shape

    for x, y in coordinates:
        if (x + tile_width) >= image_width or (y + tile_height) >= image_height:
            print("invalid")
        else:
            tile = np.array(image[y:y + tile_height, x:x + tile_width])
            yield tile

image_size = (800, 800)  
tile_size = (100, 100)   
slide_x = 50             
slide_y = 50           

image = np.random.rand(image_size[0], image_size[1])
coordinates = coordinate_generator(image_size, tile_size, slide_x, slide_y)
tiles = tile_generator(image, tile_size, coordinates)

for tile in tiles:
    print(tile.shape)
    print(tile)