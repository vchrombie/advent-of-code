import re

INPUT_FILE = 'inputs/13.txt'
SAMPLE_FILE = 'inputs/sample/13.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

A = [(int(m.group(1)), int(m.group(2)))
     for line in lines
     if (m := re.search(r'Button A: X\+(\d+), Y\+(\d+)', line))]
B = [(int(m.group(1)), int(m.group(2)))
     for line in lines
     if (m := re.search(r'Button B: X\+(\d+), Y\+(\d+)', line))]
PRIZE = [(int(m.group(1)), int(m.group(2)))
         for line in lines
         if (m := re.search(r'Prize: X=(\d+), Y=(\d+)', line))]


def solve(ax, ay, bx, by, x, y):
    # matrix representation
    # | ax ay | | a | = | x |
    # | bx by | | b |   | y |

    mat_div = ax * by - bx * ay
    na, ra = divmod(by * x - bx * y, mat_div)
    nb, rb = divmod(ax * y - ay * x, mat_div)
    if na >= ra == 0 == rb <= nb:
        return (na, nb)

    return None


def part1():
    tokens = 0
    buttons = []

    for (ax, ay), (bx, by), (x, y) in zip(A, B, PRIZE):
        solution = solve(ax, ay, bx, by, x, y)
        if solution:
            buttons.append(solution)

    for button in buttons:
        a, b = button
        tokens += ((a * 3) + (b * 1))

    print(tokens)


def part2():
    tokens = 0
    buttons = []

    for (ax, ay), (bx, by), (x, y) in zip(A, B, PRIZE):
        x += 10000000000000
        y += 10000000000000
        solution = solve(ax, ay, bx, by, x, y)
        if solution:
            buttons.append(solution)

    for button in buttons:
        a, b = button
        tokens += ((a * 3) + (b * 1))

    print(tokens)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
