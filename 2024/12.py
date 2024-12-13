from collections import deque

INPUT_FILE = 'inputs/12.txt'
SAMPLE_FILE = 'inputs/sample/12.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

MAP = [list(line.strip()) for line in lines]
ROWS = len(MAP)
COLS = len(MAP[0])

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def get_neighbours(cell):
    r, c = cell
    neighbours = []

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            neighbours.append((nr, nc))

    return neighbours


def get_cardinal_neighbours(cell, grid=None):
    r, c = cell
    neighbours = []

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if not grid or (0 <= nr < ROWS and 0 <= nc < COLS):
            neighbours.append((nr, nc))

    return neighbours


def get_diagonal_neighbours(cell):
    r, c = cell
    neighbours = []

    for dr, dc in DIAGONAL_DIRECTIONS:
        nr, nc = r + dr, c + dc
        neighbours.append((nr, nc))

    return neighbours


def build_region(start_cell):
    cell_content = MAP[start_cell[0]][start_cell[1]]
    to_visit = deque([start_cell])
    region = set()

    while to_visit:
        cell = to_visit.pop()
        if cell in region:
            continue
        region.add(cell)
        for neighbour in get_neighbours(cell):
            if MAP[neighbour[0]][neighbour[1]] == cell_content:
                to_visit.append(neighbour)

    return region


def generate_regions():
    regions = []
    visited = set()

    for idx, row in enumerate(MAP):
        for idy, _ in enumerate(row):
            cell = (idx, idy)
            if cell not in visited:
                region = build_region(cell)
                visited.update(region)
                regions.append(region)

    return regions


def calculate_perimeter(region):
    perimeter = 0
    for cell in region:
        for neighbour in get_cardinal_neighbours(cell):
            if neighbour not in region:
                perimeter += 1

    return perimeter


def count_corners(region, cell):
    corners = 0
    up, down, left, right = get_cardinal_neighbours(cell)
    up_left, up_right, down_left, down_right = get_diagonal_neighbours(cell)

    def add_corner(condition):
        nonlocal corners
        if condition:
            corners += 1

    # check corners for the "up" side
    add_corner(up in region and left in region and up_left not in region)
    add_corner(up in region and right in region and up_right not in region)
    add_corner(up not in region and left not in region)
    add_corner(up not in region and right not in region)

    # check corners for the "down" side
    add_corner(down in region and left in region and down_left not in region)
    add_corner(down in region and right in region and down_right not in region)
    add_corner(down not in region and left not in region)
    add_corner(down not in region and right not in region)

    return corners


def calculate_number_of_sides(region):
    sides = 0
    for cell in region:
        sides += count_corners(region, cell)

    return sides


def part1():
    result = 0

    regions = generate_regions()
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region)
        result += area * perimeter

    print(result)


def part2():
    result = 0

    regions = generate_regions()
    for region in regions:
        area = len(region)
        sides = calculate_number_of_sides(region)
        result += area * sides

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
