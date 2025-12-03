import re

import numpy as np
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('03', debug_mode)

    grid = np.zeros((1000, 1000))
    overlapping = set()
    overlapped_fields = set()
    ids = set()

    for line_index, line in enumerate(lines):
        id, lm, tm, width, height = [int(x) for x in re.findall(r'\d+', line)]
        ids.add(id)
        for i in range(lm, lm + width):
            for j in range(tm, tm + height):
                if grid[j,i] > 0:
                    overlapping.add(grid[j,i])
                    overlapping.add(id)
                    overlapped_fields.add((i,j))
                grid[j,i] = id

    print(len(overlapped_fields))

    for id in ids:
        if id not in overlapping:
            print(id)
            break

if __name__ == '__main__':
    do_main(False)