from itertools import product
from functools import cache

INPUT_FILE = 'inputs/21.txt'
SAMPLE_FILE = 'inputs/sample/21.txt'

NUMERIC = "789456123 0A"
DIRECTIONAL = " ^A<v>"

with open(INPUT_FILE) as f:
    lines = f.readlines()

CODES = [line.strip() for line in lines]


@cache
def paths(keymap):
    # precomputes paths between all pairs of keys on the keypad

    locations = {
        c: (x, y)
        for y, row in enumerate(keymap[i:i + 3] for i in range(0, len(keymap), 3))
        for x, c in enumerate(row)
    }

    pathmap = {}

    for a, b in product((c for c in keymap if c != ' '), repeat=2):
        if a == b:
            # no movement needed if keys are the same
            pathmap[a, b] = ['']
            continue

        (ax, ay), (bx, by) = locations[a], locations[b]
        dx, dy = bx - ax, by - ay

        # movements in x and y directions
        moves_x = '>' * max(0, dx) + '<' * max(0, -dx)
        moves_y = 'v' * max(0, dy) + '^' * max(0, -dy)

        # if gap is not in the way, both orders of movement are valid
        if dx == 0 or dy == 0 or locations[' '] not in [(bx, ay), (ax, by)]:
            pathmap[a, b] = [moves_x + moves_y, moves_y + moves_x]
        # if gap is in the way horizontally, move vertically first
        elif locations[' '] == (bx, ay):
            pathmap[a, b] = [moves_y + moves_x]
        # if gap is in the way vertically, move horizontally first
        else:
            pathmap[a, b] = [moves_x + moves_y]

    return pathmap


@cache
def presses(code, depth, keypad=NUMERIC):
    # number of button presses needed for a given depth of robots
    if depth == 1:
        # only one robot, number of presses is the length of the code
        return len(code)

    keypaths = paths(keypad)
    return sum(
        min(presses(path + 'A', depth - 1, DIRECTIONAL)
            for path in keypaths[pair])
        for pair in zip('A' + code, code)
    )


def part1():
    # 2 robots

    result = 0
    for code in CODES:
        complexity = presses(code, 2 + 2) * int(code[:-1])
        result += complexity

    print(result)


def part2():
    # 25 robots

    result = 0
    for code in CODES:
        complexity = presses(code, 25 + 2) * int(code[:-1])
        result += complexity

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
