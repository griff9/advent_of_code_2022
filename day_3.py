with open("input_3.txt", "r") as file:
    data = file.read()
data = data.split('\n')

def priority(common) ->int:
    if common.isupper():
        return ord(common) - ord('A') + 27
    else:
        return ord(common) - ord('a') + 1

############################# Part 1
total = 0
for sack in data:
    mid = len(sack)//2
    a, b = set(sack[:mid]), set(sack[mid:])
    common = list(a & b)[0]
    total += priority(common)

print(f'Answer 1: {total}')

############################# Part 2
total = 0
for i in range(0,len(data),3):
    a, b, c = set(data[i]), set(data[i+1]), set(data[i+2])
    common = list(a & b & c)[0]
    total += priority(common)

print(f'Answer 2: {total}')
