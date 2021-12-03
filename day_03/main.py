from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper
from statistics import multimode


class Day3DataWrapper (DataWrapper):

    @staticmethod
    def factory(data):
        return Day3DataWrapper(data)

    def get_bit_string(self) -> str:
        return self.data

    def get_bit_at(self, index: int):
        return self.data[index]

    def get_most_common_at(self, index: int) -> []:
        return [x.get_bit_at[index] for x in self]


def get_most_common_bit(data: [], index: int) -> str:
    mode = multimode([x.get_bit_at(index) for x in data])
    if len(mode) == 1:
        return mode[0]
    else:
        return "1"


def get_least_common_bit(data: [], index: int) -> str:
    result = "1"
    if get_most_common_bit(data, index) == "1":
        result = "0"
    return result


def most_common_bits_for_string(data: []) -> str:
    result = ""
    end = len(data[0].get_bit_string())
    for index in range(end):
        result += get_most_common_bit(data, index)

    return result


def invert_bits(bit_string: str) -> str:
    result = ""
    for char in bit_string:
        result += "0" if char == "1" else "1"
    return result


def filter_list_by_mask(data: [], value: str, index: int) -> []:
    return [x for x in data if x.get_bit_at(index) == value]


def answer_one(data: []):
    gamma_rate = most_common_bits_for_string(data)
    epsilon_rate = invert_bits(gamma_rate)

    print("answer one -------------------")
    print("gamma:", gamma_rate, int(gamma_rate, 2))
    print("epsilon_rate:", epsilon_rate, int(epsilon_rate, 2))
    print("answer:", int(gamma_rate, 2) * int(epsilon_rate, 2))
    print("")


def loop(data: [], func_get_least_or_most_common_bit) -> str:
    offset = 0
    while True:
        mask = func_get_least_or_most_common_bit(data, offset)
        data = filter_list_by_mask(data, mask, offset)
        offset += 1
        if len(data) == 1:
            break

    return data[0].get_bit_string()


def answer_two(data: []):
    print("answer Two -------------------")
    oxygen_generator_rating = loop(data.copy(), get_most_common_bit)
    co2_scrubber_rating = loop(data.copy(), get_least_common_bit)

    print("oxygen_generator_rating:", oxygen_generator_rating, int(oxygen_generator_rating, 2))
    print("CO2_scrubber_rating:", co2_scrubber_rating, int(co2_scrubber_rating, 2))
    print("answer:", int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))


if __name__ == "__main__":
    list_of_data = ObjectMother("input.txt").return_list(Day3DataWrapper.factory)

    answer_one(list_of_data.copy())
    answer_two(list_of_data.copy())








