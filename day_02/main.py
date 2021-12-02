from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class DataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_direction(self) -> str:
        return self.data.split(" ")[0]

    def get_value(self) -> int:
        return int(self.data.split(" ")[1])


def loop(list_commands: []) -> (int, int, int):
    horizontal, aim, depth = 0, 0, 0

    for data in list_commands:
        if data.get_direction() == "forward":
            horizontal += data.get_value()
            depth += aim * data.get_value()
        elif data.get_direction() == "up":
            aim -= data.get_value()
        elif data.get_direction() == "down":
            aim += data.get_value()
        else:
            print("curious")

    return horizontal, depth, aim


if __name__ == "__main__":
    x, y, angle = loop(ObjectMother("input.txt").return_list(DataWrapper.factory))

    print("Question 1:- horizontal: ", x, " depth: ", angle, "answer: ", x * angle)
    print("Question 2:- horizontal: ", x, " depth: ", y, "answer: ", x * y)
