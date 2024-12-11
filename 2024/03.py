import re

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def mul(mul_str):
    a, b = mul_str[4:-1].split(',')
    return int(a) * int(b)


def part1():
    result = 0

    pattern = re.compile(r"mul\(\d+,\d+\)")
    for line in lines:
        matches = pattern.findall(line)
        for match in matches:
            result += mul(match)

    print(result)


def part2():
    result = 0
    flag = True

    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    for line in lines:
        matches = pattern.findall(line)
        for match in matches:
            if match == "do()":
                flag = True
            elif match == "don't()":
                flag = False
            elif flag:
                result += mul(match)

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
