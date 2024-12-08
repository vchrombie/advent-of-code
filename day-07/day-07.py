from itertools import product

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

data = []
for line in lines:
    target, numbers = line.split(":")
    target = int(target)
    nums = list(map(int, numbers.split()))
    data.append((target, nums))


def evaluate_expression_part1(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
    return result


def is_equation_valid_part1(target, nums):
    num_operators = len(nums) - 1
    for ops in product(['+', '*'], repeat=num_operators):
        if evaluate_expression_part1(nums, ops) == target:
            return True
    return False


def part1():
    result = 0

    for target, nums in data:
        if is_equation_valid_part1(target, nums):
            result += target

    print(result)


def evaluate_expression_part2(nums, ops):
    def concatenate(a, b):
        return int(f"{a}{b}")

    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
        elif op == '||':
            result = concatenate(result, nums[i + 1])
    return result


def is_equation_valid_part2(target, nums):
    num_operators = len(nums) - 1
    for ops in product(['+', '*', '||'], repeat=num_operators):
        if evaluate_expression_part2(nums, ops) == target:
            return True
    return False


def part2():
    result = 0

    for target, nums in data:
        if is_equation_valid_part2(target, nums):
            result += target

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
