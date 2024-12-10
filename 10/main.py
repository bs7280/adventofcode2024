test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

test_data2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""


def add_pts(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]


class Grid:
    def __init__(self, grid):
        self.grid = grid

    # Make this class have the ability to do grid[i][j] like self.grid[i][j]
    def __getitem__(self, key):
        return self.grid[key]

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def set(self, pos, value):
        self.grid[pos[0]][pos[1]] = value

    def is_valid(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= len(self.grid) or pos[1] >= len(self.grid[0]):
            return False
        return True

    def copy(self):
        return Grid([list(row) for row in self.grid])

    def __len__(self):
        return len(self.grid)

    def __repr__(self) -> str:
        return "\n".join(["".join(r) for r in self.grid])


def find_path(grid, current_pos, current_path=[]):
    """
    Recursive funciton to find path down the hill
    """

    current_val = int(grid.get(current_pos))
    if len(current_path) == 0:
        current_path = [current_pos]

    deltas = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    paths = []
    forks = 0
    terminal_paths = []
    for delta in deltas:
        new_pos = add_pts(current_pos, delta)
        if grid.is_valid(new_pos):
            _pt = grid.get(new_pos)
            if _pt != "." and int(_pt) == current_val + 1:
                if int(_pt) == 9:
                    terminal_paths += [current_path + [new_pos]]
                else:
                    forks += 1
                    path = find_path(
                        grid, new_pos, current_path=current_path + [new_pos]
                    )
                    if path:
                        paths += path

    if len(terminal_paths) > 0:
        return terminal_paths
    if forks == 0:
        return False
    else:
        return paths


def p1(data):
    data = Grid([list(r) for r in data.split("\n")])

    low_points = []
    high_points = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "0":
                low_points.append((i, j))
            if data[i][j] == "9":
                high_points.append((i, j))

    # print(low_points)
    # print(high_points)

    paths = []
    score = 0
    trailhead_rating = 0
    for start in low_points:
        end_pts = []
        distinct_paths = []
        # breakpoint()
        result = find_path(data, start)
        if result:
            paths += result
            trailhead_rating += len(set([str(r) for r in result if r[-1] is not None]))
            for r in result:
                if r[-1] is not None:
                    end_pts.append(r[-1])
        score += len(set(end_pts))
        trailhead_rating += len(distinct_paths)
    print(score, trailhead_rating)


p1(test_data)

with open("data.txt", "r") as f:
    data = f.read()
p1(data)
