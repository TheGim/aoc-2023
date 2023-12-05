class Mapping:
    def __init__(self, tuples):
        self.tuples = tuples

    def apply_one(self, x):
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, ranges):
        adjusted_ranges = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            ranges = self.adjust_ranges(ranges, dest, src, src_end, adjusted_ranges)
        return adjusted_ranges + ranges

    def adjust_ranges(self, ranges, dest, src, src_end, adjusted_ranges):
        new_ranges = []
        while ranges:
            (start, end) = ranges.pop()
            before, intersect, after = self.calculate_ranges(start, end, src, src_end)
            self.append_new_ranges(new_ranges, before, intersect, after, dest, src, adjusted_ranges)
        return new_ranges

    def calculate_ranges(self, start, end, src, src_end):
        before = (start, min(end, src))
        intersect = (max(start, src), min(src_end, end))
        after = (max(src_end, start), end)
        return before, intersect, after

    def append_new_ranges(self, new_ranges, before, intersect, after, dest, src, adjusted_ranges):
        if before[1] > before[0]:
            new_ranges.append(before)
        if intersect[1] > intersect[0]:
            adjusted_ranges.append((intersect[0] - src + dest, intersect[1] - src + dest))
        if after[1] > after[0]:
            new_ranges.append(after)



def parse_input(input_string):
    parts = input_string.split('\n\n')
    seed = list(map(int, parts[0].split(':')[1].split()))
    mappings = [Mapping([list(map(int, line.split())) for line in part.split('\n')[1:]]) for part in parts[1:]]
    return mappings, seed

def find_min_location(mappings, seeds):
    min_locations = []
    for seed in seeds:
        for mapping in mappings:
            seed = mapping.apply_one(seed)
        min_locations.append(seed)
    return min(min_locations)

def find_min_location_part2(mappings, seeds):
    min_locations = []
    for (start, size) in zip(seeds[::2], seeds[1::2]):
        ranges = [(start, start + size)]
        for mapping in mappings:
            ranges = mapping.apply_range(ranges)
        min_locations.append(min(x for (x, _) in ranges))
    return min(min_locations)

def main():
    with open('Day5_/input.txt', 'r') as file:
        input_string = file.read().strip()
    mappings, seeds = parse_input(input_string)
    min_location1 = find_min_location(mappings, seeds)
    print(min_location1)
    min_location2 = find_min_location_part2(mappings, seeds)
    print(min_location2)

main()