from typing import Tuple

from PIL import Image

def get_average_colors(image: Image) -> Tuple[int, int, int]:
    pixel_values = list(image.getdata())

    rgb = [0, 0, 0]

    for pixel in pixel_values:
        for i in range(3):
            rgb[i] += pixel[i]

    pixels_num = len(pixel_values)

    for i in range(3):
        rgb[i] /= pixels_num

    return rgb
