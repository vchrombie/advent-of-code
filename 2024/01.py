INPUT_FILE = 'input.txt'
INPUT_FILE = 'inputs/11.txt'
SAMPLE_FILE = 'inputs/sample/11.txt'


nums = []

with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()

nums1, nums2 = [], []
for line in lines:
    nums = line.strip().split('   ')
    nums1.append(int(nums[0]))
    nums2.append(int(nums[1]))


def part1():
    result = 0

    for num1, num2 in zip(sorted(nums1), sorted(nums2)):
        result += abs(num1 - num2)

    print(result)


def part2():
    result = 0

    from collections import Counter
    nums2_counter = Counter(nums2)

    for i in nums1:
        if i in nums2_counter.keys():
            result += i * nums2_counter[i]

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
