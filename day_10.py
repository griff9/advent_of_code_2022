with open("inputs\input_10.txt", "r") as file:
    data = file.read()
data = data.split("\n")


x = 1  # sprite position
cycle = 0
crt = ["."] * 40
total = 0


def check():
    global total, cycle, crt
    if x - 1 <= cycle % 40 <= x + 1:
        crt[cycle % 40] = "#"

    cycle += 1

    if cycle != 0 and (cycle == 20 or (cycle - 60) % 40 == 0):
        total += x * cycle
    if cycle % 40 == 0 and cycle != 0:
        print("".join(crt))
        crt = ["."] * 40


for j, row in enumerate(data):
    check()
    if "addx" in row:
        check()
        _, val = row.split()
        x += int(val)

############################# Part 1
print(f"Answer 1: {total}")
