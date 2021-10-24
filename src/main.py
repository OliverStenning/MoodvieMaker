import sys
from typing import List

import numpy as np

import read
from process import get_average_color_numpy, get_dominant_color, show_average_and_dominant_colors, get_average_colors
from save import create_svg


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 3:
        raise Exception(
            f"Found {num_args} args - expected 3: COMMAND <video name> <video path>"
        )

    _, name, path = sys.argv
    frames = read.read_frames(path, 60*24)
    print(f"Found {len(frames)} video frames")

    avg_colors: List[np.ndarray] = []
    dom_colors: List[np.ndarray] = []
    for i in range(len(frames)):
        avg_colors.append(get_average_color_numpy(frames[i]).astype(int))
        dom_colors.append(get_average_colors(frames[i]).astype(int))
        print(i)
        

    create_svg(avg_colors, dom_colors)

    print("Done!")
