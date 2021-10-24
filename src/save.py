import svgwrite
from svgwrite.shapes import Rect
from numpy import ndarray

COLOR_WIDTH = 100
COLOR_HEIGHT = 10

def create_svg(colors: list(ndarray)):
    dwg = svgwrite.Drawing('test.svg', profile='none')

    position = 0

    for color in colors:
        colorString = 'rgb(' + color[0] + ',' + color[1] + ',' + color[2] + ')'
        dwg.add(Rect(insert=(0, position), size=(COLOR_WIDTH, COLOR_HEIGHT), fill=colorString))
        position += COLOR_HEIGHT

    dwg.save()
