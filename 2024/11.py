from collections import defaultdict

INPUT_FILE = 'inputs/11.txt'
SAMPLE_FILE = 'inputs/sample/11.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def read_stones():
    stones = defaultdict(int)
    for stone in lines[0].split():
        stones[int(stone)] += 1

    return stones


def transform(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone, n = str(stone), len(str(stone)) // 2
        return [int(stone[:n]), int(stone[n:])]
    else:
        return [stone * 2024]


def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        for new_stone in transform(stone):
            new_stones[new_stone] += count

    return new_stones


def part1():
    stones = read_stones()
    for _ in range(0, 25):
        stones = blink(stones)

    print(sum(stones.values()))


def part2():
    stones = read_stones()
    for _ in range(0, 75):
        stones = blink(stones)

    print(sum(stones.values()))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
