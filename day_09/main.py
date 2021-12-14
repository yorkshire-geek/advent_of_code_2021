from pathlib import Path


def get_value_or_9(x: int, y: int) -> int:
    if y == -1 or x == -1 or y == len(data) or x == len(data[0]):
        return 9

    return data[y][x]


def is_low_point(x: int, y: int) -> bool:
    above = get_value_or_9(x, y-1)
    below = get_value_or_9(x, y+1)
    right = get_value_or_9(x+1, y)
    left = get_value_or_9(x-1, y)
    value = data[y][x]

    return (value < above) and (value < below) and (value < right) and (value < left)


def get_neighbours(x: int, y: int) -> []:
    above = get_value_or_9(x, y-1)
    below = get_value_or_9(x, y+1)
    right = get_value_or_9(x+1, y)
    left = get_value_or_9(x-1, y)


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

    low_points = get_low_points()

    risk_level = 0
    for low_point in low_points:
        risk_level += data[low_point[1]][low_point[0]] + 1
        print(low_point, "-", data[low_point[1]][low_point[0]])
    print("answer:", risk_level)
