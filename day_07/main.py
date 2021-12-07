from pathlib import Path


def do_it(function) -> int:
    ans = []
    for n in range(0, max(data)):
        ans.append(sum([function(x-n) for x in data]))

    return min(ans)


def sum_of_series(value: int) -> int:
    return int((abs(value) * (abs(value) + 1)) / 2)


if __name__ == "__main__":
    data = ([int(x) for x in Path('input.txt').read_text().strip().split(",")])
    # print(data)
    # print(max(data))

    print("question 1:", do_it(abs))
    print("question 2:", do_it(sum_of_series))



