INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

map = [list(line.strip()) for line in lines]

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

TURN_RIGHT = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def get_initial_position(map):
    for idx, row in enumerate(map):
        for jdx, elem in enumerate(row):
            if elem in DIRECTIONS.keys():
                return (idx, jdx), elem


def find_path(map):
    current_pos, current_dir = get_initial_position(map)
    positions = set()
    rows, cols = len(map), len(map[0])

    while True:
        positions.add(current_pos)
        dr, dc = DIRECTIONS[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        next_r, next_c = next_pos
        if map[next_r][next_c] == '#':
            current_dir = TURN_RIGHT[current_dir]
        else:
            current_pos = next_pos

    return positions


def find_path_cycle(map, input_pos, input_dir):
    positions = set((input_pos, input_dir))
    min_row, max_row = 0, len(map)
    min_col, max_col = 0, len(map[0])

    current_pos = input_pos
    current_dir = input_dir

    while True:
        if (current_pos, current_dir) in positions:
            return True

        positions.add((current_pos, current_dir))

        dr, dc = DIRECTIONS[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        if not (min_row <= next_pos[0] < max_row and min_col <= next_pos[1] < max_col):
            break

        next_r, next_c = next_pos
        if map[next_r][next_c] == '#':
            current_dir = TURN_RIGHT[current_dir]
        else:
            current_pos = next_pos

    return False


def part1():
    result = len(find_path(map))
    print(result)


def part2():
    result = 0

    visited = find_path(map)
    initial_pos, initial_dir = get_initial_position(map)

    for obstruction in visited:
        new_map = [row[:] for row in map]
        or_r, or_c = obstruction
        new_map[or_r][or_c] = '#'

        if find_path_cycle(new_map, initial_pos, initial_dir):
            result += 1

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
