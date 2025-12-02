from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('01', debug_mode)

    point_sum = 0
    point_sum2 = 0
    seen = set()
    res2 = None

    for line_index, line in enumerate(lines):
        point_sum += int(line[1:]) if line.startswith('+') else -int(line[1:])

    while not res2:
        for line_index, line in enumerate(lines):
            point_sum2 += int(line[1:]) if line.startswith('+') else -int(line[1:])
            if not res2 and point_sum2 in seen:
                res2 = point_sum2
            seen.add(point_sum2)

    print(point_sum)
    print(res2)

if __name__ == '__main__':
    do_main(False)