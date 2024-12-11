INPUT_FILE = 'sample.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.read().splitlines()

grid = [[int(x) if x.isdigit() else -1 for x in line] for line in lines]


def find_trailheads(grid):
    trailheads = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                trailheads.append((x, y))

    return trailheads


def find_valid_moves(x, y, grid):
    valid_moves = []
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < rows and 0 <= next_y < cols:
            valid_moves.append((next_x, next_y))

    return valid_moves


def find_reachable_nines(start_x, start_y, grid):
    # BFS
    visited = set()
    reachable_nines = set()

    from collections import deque
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, height = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for next_x, next_y in find_valid_moves(x, y, grid):
            next_height = grid[next_x][next_y]
            if next_height == height + 1:
                queue.append((next_x, next_y, next_height))

    return reachable_nines


def calculate_rating(start_x, start_y, grid):
    # DFS
    visited = set()
    path_count = 0

    def dfs(x, y, height):
        nonlocal path_count
        if grid[x][y] == 9:
            path_count += 1
            return

        visited.add((x, y))

        for next_x, next_y in find_valid_moves(x, y, grid):
            next_height = grid[next_x][next_y]
            if next_height == height + 1 and (next_x, next_y) not in visited:
                dfs(next_x, next_y, next_height)

        visited.remove((x, y))

    dfs(start_x, start_y, 0)
    return path_count


def part1():
    result = 0

    trailheads = find_trailheads(grid)
    for x, y in trailheads:
        result += len(find_reachable_nines(x, y, grid))

    print(result)


def part2():
    result = 0

    trailheads = find_trailheads(grid)
    for x, y in trailheads:
        result += calculate_rating(x, y, grid)

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
