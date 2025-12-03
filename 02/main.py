from collections import Counter
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('02', debug_mode)

    point_sum_2 = 0
    point_sum_3 = 0

    for line_index, line in enumerate(lines):
        counts = Counter(line)
        if 2 in counts.values():
            point_sum_2 += 1
        if 3 in counts.values():
            point_sum_3 += 1

        for line2 in lines[line_index:]:
            dist = 0
            last_bad = 0
            for i, c in enumerate(line):
                if c != line2[i]:
                    dist+=1
                    last_bad = i
            if dist == 1:
                print(line[:last_bad]+line[last_bad+1:])
    print(point_sum_2*point_sum_3)

if __name__ == '__main__':
    do_main(False)