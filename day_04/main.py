def setup_sequence(data: str):
    return [int(x) for x in data.split(",")]


def setup_card(line_number: int, data: []) -> []:
    card = []
    for m in range(1, 6):
        card.append([int(x) for x in data[line_number + m].split()])

    return card


def setup():
    with open(file_name) as f:
        lines = f.read().splitlines()

    sequence.append(setup_sequence(lines[0]))

    for n in range(1, len(lines)):
        if (lines[n]) == "":
            cards.append(setup_card(n, lines))


if __name__ == "__main__":
    sequence = []
    cards = []
    file_name = 'input_test.txt'

    setup()
    print(sequence)

    print(cards)
