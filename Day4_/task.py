def split_card(card: str) -> tuple:
    return [side.split() for side in card.strip().split(': ')[1].split(' | ')]

def score_card(card: str) -> int:
    winning, yours = split_card(card)
    return sum(1 for n in yours if n in winning)

def read_file(filepath: str) -> list:
    with open(filepath, "r") as f:
        return [line for line in f]

def part_1(filepath: str) -> int:
    data = read_file(filepath)
    return sum(int(2 ** (score_card(line) - 1)) for line in data)

def part_2(filepath: str) -> int:
    data = read_file(filepath)
    card_counter = [1] * len(data)
    for i, card in enumerate(data):
        score = score_card(card)
        for j in range(1, score + 1):
            card_counter[i + j] += card_counter[i]
    return sum(card_counter)

print(part_1("Day4_/input.txt"))
print(part_2("Day4_/input.txt"))