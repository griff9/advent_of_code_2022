
with open("inputs\input_6.txt", "r") as file:
    data = file.read()

def message_start(n) -> int:
    markers = set()
    for i,char in enumerate(data):
        if char in markers:
            markers = {char}
            continue
        markers.add(char)
        if len(markers)==n:
            return i + 1
    return -1

############################# Part 1
print(f'Answer 1: {message_start(4)}')

############################# Part 2
print(f'Answer 2: {message_start(14)}')
