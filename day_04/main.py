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

        # print(result)
        print(sum(result)*balls_drawn[-1])


def setup_sequence(data: str):
    return [int(x) for x in data.split(",")]


def setup_card(line_number: int, data: []) -> []:
    card = []
    for m in range(1, 6):
        card.append([int(x) for x in data[line_number + m].split()])

    return card


def setup():
    for n in range(1, len(lines)):
        if (lines[n]) == "":
            cards.append(BingoCard(setup_card(n, lines)))


def print_all_cards():
    for card in cards:
        card.print_card()


def do_we_have_winner() -> (bool, BingoCard):
    for card in cards:
        if card.is_winner():
            return True, card
    return False, None


def all_cards_are_winner() -> bool:
    for card in cards:
        if not card.is_winner():
            return False
    return True


if __name__ == "__main__":
    # sequence = []
    file_name = 'input.txt'
    with open(file_name) as f:
        lines = f.read().splitlines()
    balls_drawn = []
    cards = []
    sequence = setup_sequence(lines[0])

    setup()

    # Part one
    print("Part one ------------------")
    for n in range(0, len(sequence)):
        balls_drawn.append(sequence[n])
        winner, winning_card = do_we_have_winner()
        if winner:
            # winning_card.print_card()
            winning_card.print_score()
            break

    # Part two
    print("Part two ------------------")
    balls_drawn = sequence
    finished = False
    while not finished:
        last_value = balls_drawn.pop()
        if not all_cards_are_winner():
            filtered = filter(lambda card: card.is_winner() is False, cards)
            losing_card = list(filtered)[0]
            balls_drawn.append(last_value)
            losing_card.print_score()
            break



