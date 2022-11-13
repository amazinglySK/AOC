from collections import Counter

with open('input.txt', 'r') as input_file:
    groups = [x for x in input_file.read().strip().split('\n\n')]
    groups = [[i for i in x if i != '\n'] for x in groups]
    counts = [set(group) for group in groups]
    sums = [len(group) for group in counts]
    print(sum(sums))