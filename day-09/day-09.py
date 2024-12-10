INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

data = [int(c) for c in lines[0].strip()]


def prepare_data(data):
    full, free = [], []

    for i in range(len(data)):
        if (i % 2) == 0:
            full.append(i)
        else:
            free.append(i)

    nb_to_add = 0
    processed = []

    for i in range(len(full)):
        for _ in range(data[full[i]]):
            processed.append(nb_to_add)

        if i < len(free):
            for _ in range(data[free[i]]):
                processed.append('.')

        nb_to_add += 1

    return processed


def part1():
    checksum = 0

    processed = prepare_data(data)

    while '.' in processed:
        last = processed.pop()
        if last != '.':
            dot_index = processed.index('.')
            processed[dot_index] = last

    for i in range(len(processed)):
        checksum += i * processed[i]

    print(checksum)


def extract_blocks(processed):
    blocks = []
    current_symbol = processed[0]
    start_index = 0
    length = 0

    for i, symbol in enumerate(processed):
        if symbol == current_symbol:
            length += 1
        else:
            blocks.append((current_symbol, start_index, length))
            current_symbol = symbol
            start_index = i
            length = 1

    blocks.append((current_symbol, start_index, length))
    return blocks


def compact_files(processed):
    blocks = extract_blocks(processed)

    for symbol, start, length in reversed(blocks):
        if symbol == '.':
            continue

        for _, (free_symbol, free_start, free_length) in enumerate(blocks):
            if free_symbol == '.' and free_length >= length and free_start < start:

                processed[free_start:free_start + length] = [symbol] * length
                processed[start:start + length] = ['.'] * length

                blocks = extract_blocks(processed)
                break
    return processed


def part2():
    checksum = 0

    processed = prepare_data(data)
    processed = compact_files(processed)

    for i in range(len(processed)):
        if processed[i] != '.':
            checksum += i * processed[i]

    print(checksum)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
