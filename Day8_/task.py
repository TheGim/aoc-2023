from collections import deque
import math

def read_input(file_name):
    nodes = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        for line in lines[1:]:
            if ' = ' in line:
                node, values = line.strip().split(' = ')
                nodes[node] = tuple(values.strip('()').split(', '))

    return nodes, instructions

def solve(start, instructions, nodes):
    pos = start
    idx = 0
    while not pos.endswith('Z'):
        d = instructions[idx%len(instructions)]
        pos = nodes[pos][0 if d=='L' else 1]
        idx += 1
    return idx

nodes, instructions = read_input('input.txt')

# Part 1
pos = 'AAA'
idx = 0
while pos != 'ZZZ':
    d = instructions[idx%len(instructions)]
    pos = nodes[pos][0 if d=='L' else 1]
    idx += 1
print("p1", idx)

# Part 2
ret = 1
for start in nodes:
    if start.endswith('A'):
        ret = math.lcm(ret, solve(start, instructions, nodes))

print("p2", ret)