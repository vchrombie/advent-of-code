INPUT_FILE = 'inputs/17.txt'
SAMPLE_FILE = 'inputs/sample/17.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

regs, prog = [], []
for line in lines:
    if 'Register' in line:
        regs.append(int(line.split(': ')[1]))
    elif 'Program' in line:
        prog.extend(list(map(int, line.split(': ')[1].split(','))))


def opcode(reg, prog, verbose=False, part=1):
    i = 0
    output = []

    while i < len(prog):
        op = prog[i]      # opcode
        li = prog[i + 1]  # literal or value

        # combo value from literal or register
        co = reg[li - 4] if 3 < li < 7 else li

        if verbose:
            print(f"{i} | {op} : {co} | ", end="")

        # opcode
        if op == 0:  # adv: adjust reg[0] by right shifting co times
            reg[0] //= 2 ** co
        elif op == 1:  # bxl: XOR reg[1] with literal
            reg[1] ^= li
        elif op == 2:  # bst: set reg[1] to co modulo 8
            reg[1] = co % 8
        elif op == 3:  # jnz: jump to li if reg[0] is not zero
            if reg[0] != 0:
                i = li - 2
        elif op == 4:  # bxc: XOR reg[1] with reg[2]
            reg[1] ^= reg[2]
        elif op == 5:  # out: append co modulo 8 to output
            output.append(co % 8)
        elif op == 6:  # bdv: divide reg[0] by 2**co and store in reg[1]
            reg[1] = reg[0] // 2 ** co
        elif op == 7:  # cdv: divide reg[0] by 2**co and store in reg[2]
            reg[2] = reg[0] // 2 ** co

        if verbose:
            print(reg)

        i += 2  # move to the next instruction

    return output, reg


def part1():
    result, _ = opcode(regs, prog)
    result = "".join([str(o)+',' for o in result])[:-1]
    print(result)


def find_a(prog, a=0, b=0, c=0, ip=-1):
    # base case
    if abs(ip) > len(prog):
        return a

    for i in range(8):
        aa = a * 8 + i
        reg = [aa, b, c]
        output, reg = opcode(reg, prog)

        # check if the first output matches the program instruction at ip
        if output[0] == prog[ip]:
            result = find_a(prog, aa, reg[1], reg[2], ip - 1)

            # if a valid result is found, return it
            if result is not None:
                return result

    return None


def part2():
    result = find_a(prog)
    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
