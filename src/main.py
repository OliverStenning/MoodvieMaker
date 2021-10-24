import sys
from typing import List

import numpy as np

import read
from process import get_dominant_color
from save import create_svg


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 3:
        raise Exception(
            f"Found {num_args} args - expected 3: COMMAND <video name> <video path>"
        )

    _, name, path = sys.argv
    frames = read.read_frames(path, 300)
    print(f"Found {len(frames)} video frames")

    colors: List[np.ndarray] = []
    for i in range(len(frames)):
        colors.append(get_dominant_color(frames[i]).astype(int))
        print(i)

    create_svg(colors)

    print("Done!")
