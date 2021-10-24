import cv2
from PIL import Image

def get_average_colors(image: Image):
    w, h = image.size
    pixel_values = list(image.getdata())

    r = 0
    g = 0
    b = 0

    for pixel in pixel_values:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]

    pixels_num = len(pixel_values)

    r = r / pixels_num
    g = g / pixels_num
    b = b / pixels_num

    return (r, g, b)

# Sauce: https://stackoverflow.com/a/48602446/4752388
def opencv_image_to_pillow_image(opencv_image) -> Image:
    rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    return pil_image
