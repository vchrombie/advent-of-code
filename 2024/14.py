INPUT_FILE = 'inputs/14.txt'
SAMPLE_FILE = 'inputs/sample/14.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

ROBOTS = []
for line in lines:
    line = line.split()
    y, x = map(int, line[0][2:].split(','))
    vy, vx = map(int, line[1][2:].split(','))
    ROBOTS.append([y, x, vy, vx])

WIDTH, HEIGHT = 103, 101


def step(pos, vel, t):
    # move the robot by t seconds
    y, x = pos
    dy, dx = vel

    x += (dx * t)
    y += (dy * t)

    x %= WIDTH
    y %= HEIGHT

    return x, y


def part1():
    result = 1
    quadrants = [0] * 4

    for i, j in (step(robot[:2], robot[2:], 100) for robot in ROBOTS):
        half_width = (WIDTH >> 1) + 1
        half_height = (HEIGHT >> 1) + 1

        x, rx = divmod(i, half_width)
        y, ry = divmod(j, half_height)

        if rx == half_width - 1 or ry == half_height - 1:
            continue

        quadrants[x * 2 + y] += 1

    for quadrant in quadrants:
        result *= quadrant

    print(result)


def draw(curr):
    print()
    grid = [['.'] * HEIGHT for _ in range(WIDTH)]
    for i, j in curr:
        grid[i][j] = '#'

    print('\n'.join(''.join(row) for row in grid))


def part2():
    # the idea is the easter egg will be visible when
    # no two robots are in the same position

    t = 1
    while True:
        cur = {step(robot[:2], robot[2:], t) for robot in ROBOTS}
        if len(cur) == len(ROBOTS):
            print(t)
            draw(cur)
            break
        t += 1


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
