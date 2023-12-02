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


pattern = re.compile(r'\d')
#pattern = re.compile(r'(?=(' + '|'.join(num_word_map.keys()) + r'|\d))')



def get_number(num) -> str:
    return num if num.isdigit() else num_word_map[num]

with open ('first/input.txt', 'r') as f:
    curr_sum = sum(int(get_digit(matches[0]) + get_digit(matches[-1])) for matches in map(pattern.findall, map(str.strip, f)))
    print(curr_sum)