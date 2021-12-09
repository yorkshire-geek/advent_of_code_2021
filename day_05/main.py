from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper
from collections import defaultdict


class Day5DataWrapper (DataWrapper):

    @staticmethod
    def factory(data):
        return Day5DataWrapper(data)

    def get_start_xy(self) -> int:
        return int(self.data.split(" -> ")[0].split(",")[0]), int(self.data.split(" -> ")[0].split(",")[1])

    def get_end_xy(self):
        return int(self.data.split(" -> ")[1].split(",")[0]), int(self.data.split(" -> ")[1].split(",")[1])

    def get_data(self) -> []:
        return self.data


def setup_dictionary():
    for y in range(0, STOP):
        for x in range(0, STOP):
            dictionary[x][y] = 0


def print_dictionary():
    for y in range(0, STOP):
        print(y, " ", end='')
        for x in range(0, STOP):
            print(str(dictionary[x][y]).replace("0", "."), end=' ')
        print()


def add_line(start, end):
    x1, y1 = start
    x2, y2 = end

    print("(", x1, ",", y1, ") (", x2, ",", y2, ")")

    if y1 == y2:
        if x1 < x2:
            while x1 <= x2:
                dictionary[x1][y1] = (dictionary[x1][y1] + 1)
                x1 += 1
        elif x1 > x2:
            while x1 >= x2:
                dictionary[x1][y1] = (dictionary[x1][y1] + 1)
                x1 -= 1
    elif x1 == x2:
        if y1 < y2:
            while y1 <= y2:
                dictionary[x1][y1] = (dictionary[x1][y1] + 1)
                y1 += 1
        elif y1 > y2:
            while y1 >= y2:
                dictionary[x1][y1] = (dictionary[x1][y1] + 1)
                y1 -= 1
    else:  # DIAGONAL
        if x1 > x2:
            x_mod = -1
        else:
            x_mod = 1

        if y1 > y2:
            y_mod = -1
        else:
            y_mod = 1

        while True:
            dictionary[x1][y1] = (dictionary[x1][y1] + 1)
            x1 += x_mod
            y1 += y_mod
            if x1 == x2:
                dictionary[x1][y1] = (dictionary[x1][y1] + 1)
                break


def print_intersections():
    result = 0
    for y in range(0, STOP):
        for x in range(0, STOP):
            if dictionary[x][y] > 1:
                result += 1
    return result


if __name__ == "__main__":
    STOP = 999
    dictionary = defaultdict(dict)
    setup_dictionary()

    list_of_data = ObjectMother("input.txt").return_list(Day5DataWrapper.factory)

    for line in list_of_data:
        add_line(line.get_start_xy(), line.get_end_xy())

    print_dictionary()
    print("answer: ", print_intersections())


# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
