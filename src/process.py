from typing import Tuple

from cv2 import TERM_CRITERIA_EPS, TERM_CRITERIA_MAX_ITER, KMEANS_RANDOM_CENTERS, COLOR_BGR2RGB, cvtColor, kmeans
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def get_average_colors(opencv_image) -> Tuple[int, int, int]:
    image = opencv_image_to_pillow_image(opencv_image)
    pixel_values = list(image.getdata())

    rgb = np.array([0, 0, 0])

    for pixel in pixel_values:
        for i in range(3):
            rgb[i] += pixel[i]

    pixels_num = len(pixel_values)

    for i in range(3):
        rgb[i] /= pixels_num

    return rgb


def get_average_color_numpy(opencv_image) -> np.ndarray:
    return opencv_image.mean(axis=0).mean(axis=0)


def get_dominant_color(opencv_image) -> np.ndarray:
    pixels = np.float32(opencv_image.reshape(-1, 3))
    n_colors = 3
    criteria = (TERM_CRITERIA_EPS + TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = KMEANS_RANDOM_CENTERS

    _, labels, palette = kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]

    return dominant

def show_average_and_dominant_colors(opencv_image):
    avg = get_average_color_numpy(opencv_image)
    avg_patch = np.ones(shape=opencv_image.shape, dtype=np.uint8)*np.uint8(avg)

    pixels = np.float32(opencv_image.reshape(-1, 3))
    n_colors = 3
    criteria = (TERM_CRITERIA_EPS + TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = KMEANS_RANDOM_CENTERS

    _, labels, palette = kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]

    indices = np.argsort(counts)[::-1]   
    freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
    rows = np.int_(opencv_image.shape[0]*freqs)

    dom_patch = np.zeros(shape=opencv_image.shape, dtype=np.uint8)
    for i in range(len(rows) - 1):
        dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12,6))
    ax0.imshow(avg_patch)
    ax0.set_title('Average color')
    ax0.axis('off')
    ax1.imshow(dom_patch)
    ax1.set_title('Dominant colors')
    ax1.axis('off')
    plt.show()

# Sauce: https://stackoverflow.com/a/48602446/4752388
def opencv_image_to_pillow_image(opencv_image) -> Image:
    rgb_image = cvtColor(opencv_image, COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    return pil_image
