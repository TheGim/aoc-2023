import math

def parse_game(game):
    return [{color: int(count) for count, color in (pair.split() for pair in subset.split(', '))} for subset in game]

def is_possible_game(game, cube_counts):
    return all(max(subset.get(color, 0) for subset in game) <= cube_counts[color] for color in cube_counts)

def possible_games(input_data, cube_counts):
    return [int(game_id.split()[1]) for game_id, game_data in (line.split(':') for line in input_data) if is_possible_game(parse_game(game_data.split(';')), cube_counts)]

def calculate_power(game):
    return math.prod(max(subset.get(color, 0) for subset in game) for color in ['red', 'green', 'blue'])

def total_power_of_min_sets(input_data):
    return sum(calculate_power(parse_game(game_data.split(';'))) for _, game_data in (line.split(':') for line in input_data))

with open('second/input.txt', 'r') as file:
    input_data = file.readlines()

cube_counts_part_one = {"red": 12, "green": 13, "blue": 14}
cube_counts_part_two = {"red": float('inf'), "green": float('inf'), "blue": float('inf')}

sum_of_possible_ids_part_one = sum(possible_games(input_data, cube_counts_part_one))
sum_of_power_part_two = total_power_of_min_sets(input_data)

print("Part One - Sum of possible game IDs:", sum_of_possible_ids_part_one)
print("Part Two - Sum of the power of minimum sets:", sum_of_power_part_two)