from pathlib import Path

dictionary = {
    -1: 0,
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}


def setup_dictionary(data: []):
    for x in data:
        dictionary[x] = (dictionary[x]+1)


def mutate_dictionary():
    for key in dictionary:
        if key == -1:
            continue
        dictionary[(key-1)] = dictionary[key]

    dictionary[8] = dictionary[-1]
    dictionary[6] += dictionary[-1]
    dictionary[-1] = 0


def count():
    result = 0
    for key in dictionary:
        result += dictionary[key]

    return result


if __name__ == "__main__":
    setup_dictionary([int(x) for x in Path('input.txt').read_text().strip().split(",")])

    for x in range(80):
        mutate_dictionary()
    print("question 1:", count())  # 352872

    for x in range(256):
        mutate_dictionary()
    print("question 2:", count())  # 1604361182149

