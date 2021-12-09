from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class Day8DataWrapper (DataWrapper):

    @staticmethod
    def factory(data):
        return Day8DataWrapper(data)

    def get_inputs(self):
        return self.data.split(" | ")[0].split()

    def get_outputs(self):
        return self.data.split(" | ")[1].split()


def get_all_outputs() -> []:
    result = []
    for data in list_of_data:
        result += data.get_outputs()
    return result


def get_part_one() -> int:
    jobber = list(filter(lambda output: len(output) in [2, 4, 3, 7], get_all_outputs()))
    return len(jobber)


def is_zero(value: []) -> bool:
    return set(value) == set([char for char in "abcefg"])


def is_one(value: []) -> bool:
    return set(value) == set([char for char in "cf"])


def is_two(value: []) -> bool:
    return set(value) == set([char for char in "acdeg"])


def is_three(value: []) -> bool:
    return set(value) == set([char for char in "acdfg"])


def is_four(value: []) -> bool:
    return set(value) == set([char for char in "bcdf"])


def is_five(value: []) -> bool:
    return set(value) == set([char for char in "abdfg"])


def is_six(value: []) -> bool:
    return set(value) == set([char for char in "abdefg"])


def is_seven(value: []) -> bool:
    return set(value) == set([char for char in "acf"])


def is_eight(value: []) -> bool:
    return set(value) == set([char for char in "abcdefg"])


def is_nine(value: []) -> bool:
    return set(value) == set([char for char in "abcdfg"])


def transpose(mapping: [], input_data: []) -> []:
    result = []

    ideal_wiring = ["a", "b", "c", "d", "e", "f", "g"]

    for word in input_data:
        transposed_word = ""
        for char in word:
            transposed_word += ideal_wiring[mapping.index(char)]
        result.append(transposed_word)
    return result


if __name__ == "__main__":
    list_of_data = ObjectMother("input_test.txt").return_list(Day8DataWrapper.factory)
    # print(list_of_data)

    test_wiring = ["d", "e", "a", "f", "g", "b", "c"]
    input_words = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
    print(input_words)
    transposed_words = transpose(test_wiring, input_words)
    print(transposed_words)
    # while True:
    #     jobber = transposed_words.pop()
    #     print(jobber)
    #     if is_zero(jobber):
    #         print("zero")
    #     elif is_one(jobber):
    #         print("one")
    #     elif is_two()
    #     break
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |  cdfeb fcadb cdfeb cdbaf

# dddd
# e    a
# e    a
# ffff
# g    b
# g    b
# cccc
