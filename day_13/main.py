from operator import itemgetter


def setup(file_name: str):

    with open(file_name) as file:
        lines = [x.strip() for x in file.readlines()]

    reading_coordinates = True
    for line in lines:
        if line == "":
            reading_coordinates = False
        elif reading_coordinates:
            paper.append((int(line.split(",")[0]), int(line.split(",")[1])))
        else:
            folds.append(line)


def print_grid(data: []):
    print("----------------")
    max_x = max(data, key=lambda x: x[0])[0] + 1
    max_y = max(data, key=lambda y: y[1])[1] + 1

    for y in range(max_y):
        print()
        for x in range(max_x):
            if (x, y) in data:
                print("\u25A0", end="")
            else:
                print(" ", end="")


def fold_along_y(data:[], y_axis_fold: int) -> []:
    result = []
    for (x, y) in data:
        if y > y_axis_fold:
            new_y = y_axis_fold - (y - y_axis_fold)
            result.append((x, new_y))
        else:
            result.append((x, y))

    return result


def fold_along_x(data:[], x_axis_fold: int) -> []:
    result = []
    for (x, y) in data:
        if x > x_axis_fold:
            new_x = x_axis_fold - (x - x_axis_fold)
            result.append((new_x, y))
        else:
            result.append((x, y))

    return result


if __name__ == "__main__":
    paper = []
    folds = []
    setup("input.txt")

    first_fold = folds[0]
    if "y=" in first_fold:
        jobber = fold_along_y(paper, int(first_fold.split("y=")[1]))
    else:
        jobber = fold_along_x(paper, int(first_fold.split("x=")[1]))
    print("question 1:", len(set(jobber)))

    for fold in folds:
        if "y=" in fold:
            paper = fold_along_y(paper, int(fold.split("y=")[1]))
        else:
            paper = fold_along_x(paper, int(fold.split("x=")[1]))

    print_grid(paper)
