from typing import List

import svgwrite
from svgwrite.shapes import Rect
from numpy import ndarray

COLOR_WIDTH = 5
COLOR_HEIGHT = 100
COEFF = 1.6


def create_svg(avg_colors: List[ndarray], name: str):
    dwg = svgwrite.Drawing(f"{name}.svg", profile="tiny")

    position = 0

    for i in range(len(avg_colors)):
        avg_color = avg_colors[i]
        for i in range(len(avg_color)):
            avg_color[i] *= COEFF
            if avg_color[i] > 255:
                avg_color[i] = 255

        colorString = f"rgb({str(avg_color[2])}, {str(avg_color[1])}, {str(avg_color[0])})"
        dwg.add(Rect(insert=(position, 0), size=(COLOR_WIDTH, COLOR_HEIGHT), fill=colorString))

        position += COLOR_WIDTH

    dwg.save()
