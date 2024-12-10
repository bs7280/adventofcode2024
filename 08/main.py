from itertools import combinations


def add_points(pt1, pt2):
    return pt1[0] + pt2[0], pt1[1] + pt2[1]


def mult_point(pt, n):
    return pt[0] * n, pt[1] * n


def p1(data):
    data = data.split("\n")
    data = [list(r) for r in data]

    locations = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            key = data[i][j]
            if key != ".":
                if key not in locations:
                    locations[key] = [(i, j)]
                else:
                    locations[key].append((i, j))

    antinodes = []
    for k, v in locations.items():
        # Get all combinations of pairs between items in V
        combos = list(combinations(v, 2))
        for c1, c2 in combos:
            d1 = c1[0] - c2[0], c1[1] - c2[1]
            d2 = c2[0] - c1[0], c2[1] - c1[1]

            for m in range(1, len(data) * 2):
                ant1 = add_points(c1, mult_point(d2, m))
                ant2 = add_points(c2, mult_point(d1, m))

                if 0 <= ant1[0] < len(data) and 0 <= ant1[1] < len(data[0]):
                    antinodes.append(ant1)
                if 0 <= ant2[0] < len(data) and 0 <= ant2[1] < len(data[0]):
                    antinodes.append(ant2)
    print(len(set(antinodes)))


with open("data.txt", "r") as fh:
    data = fh.read()

p1(data)
