class BingoCard:
    def __init__(self, numbers: []):
        self.numbers = numbers

    def print_card(self):
        for line in self.numbers:
            for number in line:
                numb_to_print = str(number)
                if number in balls_drawn:
                    numb_to_print = "*" + numb_to_print

                print(numb_to_print.ljust(5), end="")
            print()

    def has_winning_row(self) -> bool:
        result = False
        for line in self.numbers:
            if set(line).issubset(balls_drawn):
                result = True
                break
        return result

    def has_winning_column(self) -> bool:
        result = False
        for y in range(5):
            line = []
            for x in range(5):
                line.append(self.numbers[x][y])
            if set(line).issubset(balls_drawn):
                result = True
                break

        return result

    def is_winner(self) -> bool:
        return self.has_winning_row() or self.has_winning_column()

    def print_score(self):
        result = []
        for y in range(5):
            for x in range(5):
                value = self.numbers[x][y]
                if value not in balls_drawn:
                    result.append(value)

        print(sum(result)*balls_drawn[-1])


def setup_sequence(data: str):
    return [int(x) for x in data.split(",")]


def setup_card(line_number: int, data: []) -> []:
    card = []
    for m in range(1, 6):
        card.append([int(x) for x in data[line_number + m].split()])

    return card


def setup():
    for counter in range(1, len(lines)):
        if (lines[counter]) == "":
            cards.append(BingoCard(setup_card(counter, lines)))


def print_all_cards():
    for card in cards:
        card.print_card()


def get_first_winner_in_list() -> BingoCard:
    return list(filter(lambda card: card.is_winner(), cards))[0]


def we_have_a_winner() -> bool:
    return len(list(filter(lambda card: card.is_winner(), cards))) > 0


def all_cards_are_winner() -> bool:
    return len(list(filter(lambda card: card.is_winner() is False, cards))) == 0


def jobber():
    global sequence
    sequence = ["hello", "world"]


if __name__ == "__main__":
    file_name = 'input.txt'
    with open(file_name) as f:
        lines = f.read().splitlines()
    balls_drawn = []
    cards = []
    sequence = setup_sequence(lines[0])
    setup()
    # print_all_cards()

    # Part one
    print("Part one ------------------")
    for n in range(0, len(sequence)):
        balls_drawn.append(sequence[n])
        if we_have_a_winner():
            winning_card = get_first_winner_in_list()
            winning_card.print_score()
            break

    # Part two
    print("Part two ------------------")
    balls_drawn = sequence
    while True:
        last_value = balls_drawn.pop()
        if not all_cards_are_winner():
            filtered = filter(lambda card: card.is_winner() is False, cards)
            losing_card = list(filtered)[0]
            balls_drawn.append(last_value)
            losing_card.print_score()
            break



