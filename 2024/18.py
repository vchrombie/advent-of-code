INPUT_FILE = 'inputs/18.txt'
SAMPLE_FILE = 'inputs/sample/18.txt'


BYTES_IN = []
with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

for line in lines:
    BYTES_IN.append(tuple(map(int, line.strip().split(','))))


def adjs(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def is_valid(x, y, size, obstacles):
    return 0 <= x <= size and 0 <= y <= size and (x, y) not in obstacles


def bfs(obstacles, start, end, size):
    dist = {start: 0}
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        for nx, ny in adjs(x, y):
            if is_valid(nx, ny, size, obstacles) and (nx, ny) not in dist:
                dist[(nx, ny)] = dist[(x, y)] + 1
                queue.append((nx, ny))
                if (nx, ny) == end:
                    return dist[end]
    return float('inf')


def part1():
    size = max(max(x, y) for x, y in BYTES_IN)
    result = bfs(set(BYTES_IN[:1024]), (0, 0), (size, size), size)

    print(result)


def part2():
    result = None

    size = max(max(x, y) for x, y in BYTES_IN)
    obstacles = set()
    for (x, y) in BYTES_IN:
        obstacles.add((x, y))
        if bfs(obstacles, (0, 0), (size, size), size) == float('inf'):
            result = (x, y)
            break

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
