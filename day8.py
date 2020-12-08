def get_acc_value(filename="data/day8.dat"):
    with open(filename) as fdata:
        lines = fdata.read().splitlines()

    acc_value = 0
    steps = [0]
    second = False
    while second is not True:
        i = steps[-1]
        split = lines[i].split(" ")

        command, value = split
        if command == "acc":
            acc_value += int(value)
            steps.append(i + 1)
        elif command == "jmp":
            steps.append(i + int(value))
        else:
            steps.append(i + 1)

        if steps[-1] >= len(lines):
            second = True

        if steps[-1] in steps[:-1]:
            second = True

    return acc_value


def get_acc_value_at_terminate(filename="data/day8.dat"):
    def replace_jmp_nop(c):
        if c[0] == "jmp":
            return ["nop", c[1]]
        elif c[0] == "nop":
            return ["jmp", c[1]]
        return c

    with open(filename) as fdata:
        lines = fdata.read().splitlines()

    for j in range(len(lines)):
        acc_value = 0
        steps = [0]
        second = False
        while second is not True:
            i = steps[-1]

            split = replace_jmp_nop(lines[i].split(" ")) if i == j else lines[i].split(" ")
            command, value = split

            if command == "acc":
                acc_value += int(value)
                steps.append(i + 1)
            elif command == "jmp":
                steps.append(i + int(value))
            else:
                steps.append(i + 1)

            if steps[-1] >= len(lines):
                return acc_value

            if steps[-1] in steps[:-1]:
                second = True

    return False


assert get_acc_value(filename="data/day8-t.dat") == 5
assert get_acc_value_at_terminate(filename="data/day8-t.dat") == 8

get_acc_value()  # 2051
get_acc_value_at_terminate()  # 2304
