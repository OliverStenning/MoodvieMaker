from typing import List

import svgwrite
from svgwrite.shapes import Rect
from numpy import ndarray

COLOR_WIDTH = 5
COLOR_HEIGHT = 100


def create_svg(avg_colors: List[ndarray], dom_colors: List[ndarray]):
    dwg = svgwrite.Drawing("test.svg", profile="tiny")

    position = 0

    for i in range(len(avg_colors)):
        avg_color = avg_colors[i]
        colorString = "rgb(" + str(avg_color[0]) + "," + str(avg_color[1]) + "," + str(avg_color[2]) + ")"
        dwg.add(
            Rect(
                insert=(position, 0), size=(COLOR_WIDTH, COLOR_HEIGHT), fill=colorString
            )
        )
        
        dom_color = dom_colors[i]
        colorString = "rgb(" + str(dom_color[0]) + "," + str(dom_color[1]) + "," + str(dom_color[2]) + ")"
        dwg.add(
            Rect(
                insert=(position, COLOR_HEIGHT), size=(COLOR_WIDTH, COLOR_HEIGHT), fill=colorString
            )
        )
        position += COLOR_WIDTH

    dwg.save()
