import cv2
from PIL import Image
from typing import Tuple

def get_average_colors(image: Image) -> Tuple[int, int, int]:

    pixel_values = list(image.getdata())

    rgb = (0, 0, 0)

    for pixel in pixel_values:
        for i in range(3):
            rgb[i] += pixel[i]

    pixels_num = len(pixel_values)

    for i in range(3):
        rgb[i] /= pixels_num

    return rgb

# Sauce: https://stackoverflow.com/a/48602446/4752388
def opencv_image_to_pillow_image(opencv_image) -> Image:
    rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    return pil_image
