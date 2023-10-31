import numpy as np
from typing import Tuple, Iterable

def coordinate_generator(image_size: Tuple[int, int], tile_size: Tuple[int, int], slide_x: int, slide_y: int) -> Iterable[Tuple[int, int]]:
    image_width, image_height = image_size
    tile_width, tile_height = tile_size

    for y in range(0, image_height - tile_height + 1, slide_y):
        for x in range(0, image_width - tile_width + 1, slide_x):
            yield (x, y)

def tile_generator(image, tile_size, coordinates):
    tile_width, tile_height = tile_size

    for x, y in coordinates:
        tile = np.array(image[y:y + tile_height, x:x + tile_width])
        yield tile

image_size = (800, 600)  
tile_size = (100, 100)   
slide_x = 50             
slide_y = 50             

image = np.random.rand(image_size[0], image_size[1])
coordinates = coordinate_generator(image_size, tile_size, slide_x, slide_y)
tiles = tile_generator(image, tile_size, coordinates)