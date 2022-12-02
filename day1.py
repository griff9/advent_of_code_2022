import heapq

with open("advent_of_code\inputs\input_1.txt", "r") as file:
    data = file.read()

best = [0] * 3
for elf in data.split("\n\n"):
    current = 0
    for chunk in elf.split("\n"):
        current += int(chunk)
    third_place = heapq.heappop(best)
    new_addition = max(current, third_place)
    heapq.heappush(best, new_addition)

print(f'Answer 1: {max(best)}')
print(f'Answer 2: {sum(best)}')
