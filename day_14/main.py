
def setup(file_name):
    global polymer_template, dictionary
    with open(file_name) as file:
        lines = file.read().splitlines()
        polymer_template = lines[0]
        for data in lines[2:]:
            key = data.split(" ")[0]
            value = data.split(" ")[2]
            dictionary[key] = value


def doit(value: str) -> str:
    result = ""
    for n in range(len(value)-1):
        jobber = value[n:n+2]
        result += value[n] + dictionary[jobber]
    result += value[-1]

    return result


if __name__ == "__main__":
    polymer_template = ""
    dictionary = {}
    setup("input_test.txt")

    # print(dictionary)

    for n in range(40):
        polymer_template = doit(polymer_template)
        # print(polymer_template)

    # for jobber in set(dictionary.values()):
    #     print("", jobber, polymer_template.count(jobber))
    jobber = [polymer_template.count(char) for char in set(dictionary.values())]
    print(jobber)
    print("answer 1:", max(jobber) - min(jobber))