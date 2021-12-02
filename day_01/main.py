def exercise_1(lines: []) -> int:
    print("exercise 1 -----------------")
    previous_line = 0
    count = 0

    for line in lines:
        if previous_line == 0:
            print(line, "init")
        # elif previous_line > line:
        #     print(line, "decreased")
        elif previous_line < line:
            count += 1
            # print(line, "increased - ", count)
        # else:
        #     print(line, "ERROR *************************************")
        previous_line = line

    print("count:", count)
    return count


def exercise_2(lines: []) -> int:
    print("exercise 2 -----------------")

    size = (len(lines) - 2)

    new_list = []
    for idx in range(size):
        new_list.append((lines[idx] + lines[idx+1] + lines[idx+2]))

    return exercise_1(new_list)


if __name__ == "__main__":
    data = [int(x) for x in open('input.txt', 'r').read().strip().splitlines()]

    print("answer exercise 1:", exercise_1(data))
    print("answer exercise 2:", exercise_2(data))


