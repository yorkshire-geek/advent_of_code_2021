from pathlib import Path


def get_value_or_9(x: int, y: int) -> int:
    try:
        return data[y][x]
    except IndexError:
        return 9


def is_low_point(x: int, y: int) -> bool:
    result = False
    above = get_value_or_9(x, y-1)
    below = get_value_or_9(x, y+1)
    right = get_value_or_9(x+1, y)
    left = get_value_or_9(x-1, y)
    value = data[y][x]
    result = (value < above) and (value < below) and (value < right) and (value < left)
    # if result:
    #     print(x, y, data[y][x])
    return result


def get_low_points() -> []:
    result = []
    for x in range(len(data[0])):
        for y in range(len(data)):
            # print(x, ",", y, " - ", data[y][x])
            if is_low_point(x, y):
                result.append((x, y))
    return result


if __name__ == "__main__":
    data = []
    for line in Path('input.txt').read_text().split():
        data.append([int(x) for x in line])

    print("input data: ", data)
    answer = get_low_points()
    counter = len(answer)
    for jobber in answer:
        counter += data[jobber[1]][jobber[0]]
        print(jobber, " -", data[jobber[1]][jobber[0]])
    print("answer:", counter)

