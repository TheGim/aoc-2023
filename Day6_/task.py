def ways_to_win(time, record):
    return sum(1 for i in range(time + 1) if (time - i) * i > record)

def read_file(filepath: str):
    with open(filepath, "r") as f:
        lines = f.readlines()
        times = list(map(int, lines[0].replace('Time:', '').split()))
        records = list(map(int, lines[1].replace('Distance:', '').split()))
    return times, records

def calculate_ways(times, records):
    ways = [ways_to_win(t, r) for t, r in zip(times, records)]
    result = 1
    for w in ways:
        result *= w
    return result

times, records = read_file('Day6_/input.txt')
result = calculate_ways(times, records)

time = int(''.join(map(str, times)))
record = int(''.join(map(str, records)))

print(result)
print(ways_to_win(time, record))