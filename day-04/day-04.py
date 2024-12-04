INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

rows = len(grid)
cols = len(grid[0])


def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols


def is_xmas(text):
    return text == 'XMAS' or text[::-1] == 'XMAS'


def part1():
    result = 0

    for x in range(rows):
        for y in range(cols):

            # check horizontal
            if is_valid(x+3, y):
                text = grid[x][y] + grid[x+1][y] + grid[x+2][y] + grid[x+3][y]
                result += 1 if is_xmas(text) else 0

            # check vertical
            if is_valid(x, y+3):
                text = grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x][y+3]
                result += 1 if is_xmas(text) else 0

            # check diagonal right
            if is_valid(x+3, y+3):
                text = grid[x][y] + grid[x+1][y+1] + \
                    grid[x+2][y+2] + grid[x+3][y+3]
                result += 1 if is_xmas(text) else 0

            # check diagonal left
            if is_valid(x+3, y-3):
                text = grid[x][y] + grid[x+1][y-1] + \
                    grid[x+2][y-2] + grid[x+3][y-3]
                result += 1 if is_xmas(text) else 0

    print(result)


def is_x_mas(text):
    return text == "MMSS" or text == "SSMM" or text == "MSMS" or text == "SMSM"


def part2():
    result = 0

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if grid[x][y] == 'A':
                text = grid[x-1][y-1] + grid[x-1][y+1] + \
                    grid[x+1][y-1] + grid[x+1][y+1]
                result += 1 if is_x_mas(text) else 0

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
