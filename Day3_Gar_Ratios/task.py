import re

def read_file(file_path):
    with open(file_path) as file:
        return [list(line) for line in file.read().strip().split("\n")]


def find_parts_by_symbol(file):
    box = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    part_sum = 0
    parts_by_symbol = {}

    for i, line in enumerate(file):
        for match in re.finditer(r"\d+", ''.join(line)):
            d = int(match.group(0))
            adjacent_cells = {(i + di, j + dj) for di, dj in box for j in range(match.start(), match.end()) if 0 <= i + di < len(file) and 0 <= j + dj < len(line)}
            symbols = {pos for pos in adjacent_cells if not file[pos[0]][pos[1]].isdigit() and file[pos[0]][pos[1]] != '.'}
            if symbols:
                part_sum += d
            for symbol in symbols:
                #dictonary pos_symbol:list_numbers
                parts_by_symbol.setdefault(symbol, []).append(d)

    return part_sum, parts_by_symbol


def calculate_gear_ratios(parts_by_symbol):
    return sum(v[0]*v[1] for v in parts_by_symbol.values() if len(v) == 2)


file = read_file("Day3_Gar_Ratios/input.txt")
part_sum, parts_by_symbol = find_parts_by_symbol(file)



print("Summe der Teilnummern:" + str(part_sum))
print("Getriebeverhältnisse:" + str(calculate_gear_ratios(parts_by_symbol)))