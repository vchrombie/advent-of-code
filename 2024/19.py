from functools import cache

INPUT_FILE = 'inputs/19.txt'
SAMPLE_FILE = 'inputs/sample/19.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
index = lines.index('')

PATTERNS = lines[:index][0].split(', ')
DESIGNS = lines[index + 1:]


@cache
def is_valid(design):
    if not design:
        return True

    for pattern in PATTERNS:
        if design.startswith(pattern):
            if is_valid(design[len(pattern):]):
                return True

    return False


def part1():
    result = 0

    for design in DESIGNS:
        if is_valid(design):
            result += 1

    print(result)


@cache
def count_ways(design):
    if not design:
        return 1

    total = 0
    for pattern in PATTERNS:
        if design.startswith(pattern):
            total += count_ways(design[len(pattern):])

    return total


def part2():
    result = 0

    for design in DESIGNS:
        result += count_ways(design)

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
