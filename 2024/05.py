from collections import defaultdict

INPUT_FILE = 'input.txt'


with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
split_index = lines.index('')

rules = defaultdict(list)
for rule in lines[:split_index]:
    a, b = rule.split('|')
    rules[a].append(b)

updates = []
for update in lines[split_index + 1:]:
    updates.append(update.split(','))


def get_middle_element(update):
    return update[len(update) // 2]


def is_valid(update):
    for idx, page in enumerate(update):
        for elem in rules[page]:
            if elem in update[:idx]:
                return False

    return True


def swap(update, elem, page):
    idx = update.index(elem)
    update[update.index(page)] = elem
    update[idx] = page
    return update


def fix(update):
    if is_valid(update):
        return update

    for idx, page in enumerate(update):
        for elem in rules[page]:
            if elem in update[:idx]:
                update = swap(update, elem, page)

    return fix(update)


def part1():
    result = 0

    for update in updates:
        if is_valid(update):
            result += int(get_middle_element(update))

    print(result)


def part2():
    result = 0

    for update in updates:
        if not is_valid(update):
            update = fix(update)
            result += int(get_middle_element(update))

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
