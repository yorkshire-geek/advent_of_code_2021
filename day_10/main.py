from pathlib import Path


pairs_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

error_value_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def error_code(value: str):
    stack = []
    for char in value:
        if char in pairs_dict.keys():
            stack.append(char)
        elif char in pairs_dict.values():
            opener = stack.pop()
            if char != pairs_dict[opener]:
                return char


if __name__ == "__main__":
    totals = []
    for line_of_file in Path('input.txt').read_text().split():
        error_value = error_code(line_of_file)
        if error_value is not None:
            totals.append(error_value_dict[error_value])

    print(totals)
    print(sum(totals))