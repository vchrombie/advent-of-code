import copy

INPUT_FILE = 'inputs/15.txt'
SAMPLE_FILE = 'inputs/sample/15.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
index = lines.index('')

MAP, MOVES = lines[:index], lines[index + 1:]

MAP = [list(row) for row in MAP]
MOVES = "".join(MOVES)

DIRECTIONS = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}


def get_robot_position(map):
    for idy, row in enumerate(map):
        for idx, cell in enumerate(row):
            if cell == "@":
                return (idx, idy)


def get_moves(map, x, y, dx, dy):
    # can we move from x,y to x+dx, y+dy?

    x2, y2 = x + dx, y + dy
    block = map[y2][x2]
    cur_move = [(x, y, x2, y2)]

    if block == ".":
        return cur_move

    if block == "#":
        return None

    if block in "[]":
        neighbour_x = x2 + 1 if block == "[" else x2 - 1
        move1 = get_moves(map, x2, y2, dx, dy)
        if move1:
            if dy:  # vertical movement
                move2 = get_moves(map, neighbour_x, y2, dx, dy)
                if move2:
                    return move1 + move2 + cur_move
            else:  # horizontal movement
                return move1 + cur_move
        return None

    if block == "O":
        move1 = get_moves(map, x2, y2, dx, dy)
        return move1 + cur_move if move1 else None


def make_moves(map, moves):
    done = set()
    for x1, y1, x2, y2 in moves:
        if (x1, y1, x2, y2) not in done:
            map[y2][x2], map[y1][x1] = map[y1][x1], map[y2][x2]
            done.add((x1, y1, x2, y2))


def show_map(map):
    for row in map:
        print("".join(row))

    print()


def gps_sum(map):
    for idx, row in enumerate(map):
        for idy, cell in enumerate(row):
            if cell in "O[":
                yield 100 * idx + idy


def part1():
    MAP1 = copy.deepcopy(MAP)
    # show_map(MAP1)
    rx, ry = get_robot_position(MAP1)
    for move in MOVES:
        dx, dy = DIRECTIONS[move]
        curr_moves = get_moves(MAP1, rx, ry, dx, dy)
        if curr_moves:
            make_moves(MAP1, curr_moves)
            rx, ry = rx + dx, ry + dy

    # show_map(MAP1)
    print(sum(gps_sum(MAP1)))


def transform_map(map):
    d = {
        "#": ["#", "#"],
        ".": [".", "."],
        "O": ["[", "]"],
        "@": ["@", "."],
    }
    return [[char for block in row for char in d[block]] for row in map]


def part2():
    MAP2 = transform_map(MAP)
    # show_map(MAP2)
    rx, ry = get_robot_position(MAP2)
    for move in MOVES:
        dx, dy = DIRECTIONS[move]
        curr_moves = get_moves(MAP2, rx, ry, dx, dy)
        if curr_moves:
            make_moves(MAP2, curr_moves)
            rx, ry = rx + dx, ry + dy

    # show_map(MAP2)
    print(sum(gps_sum(MAP2)))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
