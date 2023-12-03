import re

num_word_map = {
    'one' : '1',
    'two' : '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

part1_pattern = re.compile(r'\d')
part2_pattern = re.compile(r'(?=(' + '|'.join(num_word_map.keys()) + r'|\d))')

def get_number(num) -> str:
    return num if num.isdigit() else num_word_map[num]

def calculate_sum(pattern):
    with open ('Day1_Trebuchet/input.txt', 'r') as f:
        return sum(int(get_number(matches[0]) + get_number(matches[-1])) for matches in map(pattern.findall, map(str.strip, f)))

print("Part 1 Sum: ", calculate_sum(part1_pattern))
print("Part 2 Sum: ", calculate_sum(part2_pattern))