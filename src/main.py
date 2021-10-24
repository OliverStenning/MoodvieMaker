import sys

import read
import process
import save

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 3:
        raise Exception(
            f"Found {num_args} args - expected 3: COMMAND <video name> <video path>"
        )

    _, name, path = sys.argv
    read.read_frames(name, path)
