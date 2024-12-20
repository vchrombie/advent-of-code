INPUT_FILE = 'inputs/20.txt'
SAMPLE_FILE = 'inputs/sample/20.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
GRID = [list(line) for line in lines]

for r, row in enumerate(GRID):
    for c, cell in enumerate(row):
        if cell == 'S':
            START = (r, c)
        elif cell == 'E':
            END = (r, c)


def find_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [(start, 0, [start])]  # position, steps, path
    visited.add(start)

    while queue:
        (r, c), steps, path = queue.pop(0)
        if (r, c) == end:
            return steps, path

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), steps + 1, new_path))
                visited.add((nr, nc))


def find_cheatable_pairs_in_range(path, savings, cheat_moves):
    cheats = 0
    coords_steps = {coord: i for i, coord in enumerate(path)}

    for y, x in path:
        for dy in range(-cheat_moves, cheat_moves + 1):
            for dx in range(-cheat_moves, cheat_moves + 1):
                if dy == 0 and dx == 0:
                    continue

                manhattan = abs(dy) + abs(dx)
                if manhattan > cheat_moves:
                    continue

                ny, nx = y + dy, x + dx
                if (ny, nx) in coords_steps:
                    if savings <= (coords_steps[(ny, nx)] - coords_steps[(y, x)] - manhattan):
                        cheats += 1

    return cheats


def part1():
    _, path = find_shortest_path(GRID, START, END)

    savings = 100
    cheat_moves = 2
    result = find_cheatable_pairs_in_range(path, savings, cheat_moves)

    print(result)


def part2():
    _, path = find_shortest_path(GRID, START, END)

    savings = 100
    cheat_moves = 20
    result = find_cheatable_pairs_in_range(path, savings, cheat_moves)

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
