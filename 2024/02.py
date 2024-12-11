INPUT_FILE = 'input.txt'

ll = []  # list of levels

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

for line in lines:
    li = []
    li = line.strip().split(' ')
    li = [int(i) for i in li]
    ll.append(li)


def is_positive(num):
    return num > 0


def is_negative(num):
    return num < 0


def fits_range(num, a, b):
    return a <= abs(num) <= b


def check_level_safe(diffs):
    if 0 not in diffs:
        if all(map(is_positive, diffs)) or all(map(is_negative, diffs)):
            if all(map(lambda x: fits_range(x, 1, 3), diffs)):
                return True

    return False


def calculate_diffs(levels):
    diffs = []
    for j in range(0, len(levels) - 1):
        diff = levels[j] - levels[j + 1]
        diffs.append(diff)

    return diffs


def part1():
    result = 0

    for levels in ll:
        diffs = calculate_diffs(levels)
        if check_level_safe(diffs):
            result += 1

    print(result)


def check_problem_dampener(levels, i):
    li = levels.copy()
    li.pop(i)

    diffs = calculate_diffs(li)
    return check_level_safe(diffs)


def part2():
    result = 0

    for levels in ll:
        diffs = calculate_diffs(levels)
        if check_level_safe(diffs):
            result += 1
        else:
            for i in range(0, len(levels)):
                if check_problem_dampener(levels, i):
                    result += 1
                    break

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
