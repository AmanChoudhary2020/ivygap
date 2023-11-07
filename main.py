import numpy as np
from PIL import Image
from typing import Iterable
import os
import shutil

def coordinate_generator(image_size: tuple[int, int], tile_size: tuple[int, int], slide_x: int, slide_y: int) -> Iterable[tuple[int, int]]:
    image_width, image_height, _ = image_size
    tile_width, tile_height = tile_size

    for y in range(0, image_height - tile_height + 1, slide_y):
        for x in range(0, image_width - tile_width + 1, slide_x):
            yield (x, y)

def tile_generator(image, tile_size, coordinates):
    tile_width, tile_height = tile_size

    for x, y in coordinates:
        tile = np.array(image[y:y + tile_height, x:x + tile_width])
        yield tile

def save_tiles_as_images(tiles, output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    os.makedirs(output_dir)
    
    for i, tile in enumerate(tiles):
        tile_image = Image.fromarray(tile)
        output_file_path = os.path.join(output_dir, f"tile_{i}.png")
        tile_image.save(output_file_path)

def main():
    '''
    Dummy Image:
    1  2  3  13
    4  5  6  14
    7  8  9  15
    10 11 12 16 
    '''
    # image = np.array([[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16]]) # dummy image

    # Load image
    image = np.array(Image.open("img.png"))
    image = image.reshape(image.shape[0], image.shape[1], -1)
    print(f"Image shape: {image.shape}")

    image_size = image.shape
    tile_size = (100, 100)            

    # Generate coordinates
    coordinates = coordinate_generator(image_size, tile_size, slide_x=50, slide_y=50)
    # Generate tiles using coordinates
    tiles = tile_generator(image, tile_size, coordinates)
    
    # Save tiles to output directory
    output_dir = "output_tiles"
    save_tiles_as_images(tiles, output_dir)


if __name__ == "__main__":
    main()