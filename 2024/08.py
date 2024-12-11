INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
rows, cols = len(lines), len(lines[0])

antennas = []
for idx, line in enumerate(lines):
    for idy, char in enumerate(line):
        if char != '.':
            antennas.append((idx, idy, char))


def part1():
    result = 0

    antinodes = set()
    for i, (x1, y1, freq1) in enumerate(antennas):
        for j, (x2, y2, freq2) in enumerate(antennas):
            if freq1 != freq2:
                continue

            dx, dy = x2 - x1, y2 - y1
            ax2, ay2 = x2 + dx, y2 + dy

            if 0 <= ax2 < rows and 0 <= ay2 < cols and dx != 0 and dy != 0:
                antinodes.add((ax2, ay2))

    result += len(antinodes)
    print(result)


def part2():
    result = 0

    antinodes = set()
    for i, (x1, y1, freq1) in enumerate(antennas):
        for j, (x2, y2, freq2) in enumerate(antennas):
            if freq1 != freq2:
                continue

            dx, dy = x2 - x1, y2 - y1
            ax2, ay2 = x2, y2

            while 0 <= ax2 < rows and 0 <= ay2 < cols and dx != 0 and dy != 0:
                antinodes.add((ax2, ay2))
                ax2 += dx
                ay2 += dy

    result += len(antinodes)
    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
