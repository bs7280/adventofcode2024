import numpy as np

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
test_data = np.array([list(row) for row in test_data])
data = test_data

with open("input.txt", "r") as fh:
    data = fh.readlines()
    data = np.array([list(d.strip()) for d in data])


def get_count(data):
    count = 0
    for i in range(len(data)):  # i is row
        for j in range(0, len(data[i])):  # j is column
            if (
                data[i][j] == "A"
                and (0 < i < len(data) - 1)
                and (0 < j < len(data[i]) - 1)
            ):
                if data[i - 1][j - 1] == "M":
                    if data[i + 1][j - 1] == "M":
                        if data[i + 1][j + 1] == "S":
                            if data[i - 1][j + 1] == "S":
                                count += 1
    return count


c = 0
c += get_count(data)
data = np.rot90(data)

c += get_count(data)
data = np.rot90(data)

c += get_count(data)
data = np.rot90(data)

c += get_count(data)

print(c)
