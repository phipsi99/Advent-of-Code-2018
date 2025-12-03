from collections import defaultdict

from helpers.get_input import get_lines

DIR8 = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def shortest_to(p, coordinates):
    distances = defaultdict(list)
    for c in coordinates:
        dist = manhattan(p, c)
        distances[dist].append(c)
    min_dist = min(distances.keys())
    return distances[min_dist]

def sum_dist_to_all(p, coordinates):
    distances = []
    for c in coordinates:
        dist = manhattan(p, c)
        distances.append(dist)
    return sum(distances)

def do_main(debug_mode=False):
    lines = get_lines('06', debug_mode)

    coordinates = []

    for line_index, line in enumerate(lines):
        coordinates.append(tuple(int(i) for i in line.split(", ")))

    x_vals, y_vals = zip(*coordinates)
    xmin, xmax = min(x_vals), max(x_vals)
    ymin, ymax = min(y_vals), max(y_vals)

    blacklist = []
    counts = defaultdict(int)
    valid2 = 0

    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if sum_dist_to_all((x,y), coordinates) < 10000:
                valid2 += 1
            shortest = shortest_to((x,y), coordinates)
            if len(shortest) == 1 and shortest[0] not in blacklist:
                if y == ymin or y == ymax or x == xmin or x == xmax:
                    blacklist.append(shortest[0])
                    counts[shortest[0]] = 0
                else:
                    counts[shortest[0]] += 1
    print(max(counts.values()))
    print(valid2)


if __name__ == '__main__':
    do_main(False)