test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
    "\n"
)

data = test_data

with open("input.txt", "r") as fh:
    data = fh.readlines()


search_str = "XMAS"


def get_str_from_coords(coords):

    s = "".join(
        [
            data[i][j]
            for i, j in coords
            if i >= 0 and j >= 0 and i < len(data) and j < len(data[i])
        ]
    )

    f_i = lambda x: x[0]
    f_j = lambda x: x[1]
    index = "({0},{1}-({2},{3})".format(
        min(coords, key=f_i),
        min(coords, key=f_j),
        max(coords, key=f_i),
        max(coords, key=f_j),
    )
    return s, coords


def get_count(data, search_str):
    count = 0
    coords_used = {}
    for i in range(len(data)):  # i is row
        for j in range(0, len(data[i])):  # j is column

            # Diagonals
            all_coords = [
                # Horizontals
                get_str_from_coords([((i, j - c)) for c in range(4)]),
                get_str_from_coords([((i, j + c)) for c in range(4)]),
                # Verticals
                get_str_from_coords([(i + c, j) for c in range(4)]),
                get_str_from_coords([(i - c, j) for c in range(4)]),
                # Diagonas
                get_str_from_coords([(i + c, j + c) for c in range(4)]),
                get_str_from_coords([(i - c, j + c) for c in range(4)]),
                get_str_from_coords([(i + c, j - c) for c in range(4)]),
                get_str_from_coords([(i - c, j - c) for c in range(4)]),
            ]
            for diag, coords in sorted(all_coords, key=lambda x: str(x[1])):
                if len(diag) == 4 and diag == search_str:
                    if str(coords) not in coords_used:
                        coords_used[str(coords)] = True
                        # print(coords, diag)
                        count += 1

            # "".join([data[i + c][j + c] for c in range(0, 4)])
            # "".join([data[i - c][j + c] for c in range(0, 4)])
            # "".join([data[i + c][j - c] for c in range(0, 4)])
            # "".join([data[i - c][j - c] for c in range(0, 4)])

    print(count)


get_count(data, search_str)
