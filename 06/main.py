def process_grid(data):
    gaurd_pos = 0
    grid = data.copy()
    for i in range(len(data)):
        for j in range(len(data[0])):
            char = data[i][j]

            if char == "^":
                gaurd_pos = (i, j)
                grid[i][j] = "."

    if gaurd_pos == 0:
        raise ValueError("No gaurd found")
    return gaurd_pos, grid


class Visited:
    def __init__(self):
        self.visited = list()

    def visit(self, pos: tuple, gaurd_direction):
        self.visited.append(pos + (gaurd_direction,))

    def __contains__(self, pt):
        return pt in self.visited

    def contains(self, pt):
        return pt in [(v[0], v[1]) for v in self.visited]


def increment_direction(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"


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


def print_grid(grid, visited):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (i, j) in visited:
                row[j] = "X"
        print("".join(row))


def p1(gaurd_pos, grid, verbose):

    visited = Visited()

    gaurd_direction = "N"
    visited.visit(gaurd_pos, gaurd_direction)

    iters = 0
    while len(visited.visited):

        # Move gaurd in direction
        if gaurd_direction == "N":
            new_gaurd_pos = (gaurd_pos[0] - 1, gaurd_pos[1])
        elif gaurd_direction == "E":
            new_gaurd_pos = (gaurd_pos[0], gaurd_pos[1] + 1)
        elif gaurd_direction == "S":
            new_gaurd_pos = (gaurd_pos[0] + 1, gaurd_pos[1])
        elif gaurd_direction == "W":
            new_gaurd_pos = (gaurd_pos[0], gaurd_pos[1] - 1)

        if not grid.is_valid(new_gaurd_pos):
            if verbose:
                print(f"Gaurd finished in {len(visited.visited)} steps")
            break

        if grid.get(new_gaurd_pos) == "#":
            gaurd_direction = increment_direction(gaurd_direction)
        else:
            gaurd_pos = new_gaurd_pos

            if gaurd_pos + (gaurd_direction,) in visited and len(visited.visited) > 1:
                print("Loop detected")
                return False

            visited.visit(new_gaurd_pos, gaurd_direction)

        # if iters > 10:
        #    breakpoint()

        iters += 1

    # print_grid(grid, visited.visited)
    if verbose:
        print(f"Visited {len(visited.visited)} Distinct: {len(set(visited.visited))}")

    return visited


def p2(gaurd_pos, grid):

    base_visited = p1(gaurd_pos, grid, verbose=False)
    print(
        f"Visited {len(base_visited.visited)} Distinct: {len(set(base_visited.visited))}"
    )

    import tqdm

    # Use tqdm but I want to see the progress bar over the overall of the nested loops
    loops = 0
    for i in tqdm.tqdm(range(0, len(data))):
        for j in range(len(data[0])):
            if base_visited.contains((i, j)):
                grid_iter = grid.copy()
                if grid_iter.get((i, j)) == ".":
                    grid_iter.set((i, j), "#")
                    visited = p1(gaurd_pos, grid_iter, verbose=False)
                    if visited == False:
                        loops += 1
                        print(f"Found loop with object at {i}, {j}")
    print(f"Found {loops} loops")
    # for v in visited.visited:
    #    breakpoint()


with open("data.txt", "r") as fh:
    data = fh.read()


data = [list(row) for row in data.split("\n")]
gaurd_pos, grid = process_grid(data)
grid = Grid(grid)

p1(gaurd_pos, grid, verbose=True)

p2(gaurd_pos, grid)
