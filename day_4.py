with open("input_4.txt", "r") as file:
    data = file.read()
data = data.split("\n")

res_1 = res_2 = 0

for row in data:
    a, b = row.split(",")
    a_min, a_max = a.split("-")
    b_min, b_max = b.split("-")
    a_min, a_max = int(a_min), int(a_max)
    b_min, b_max = int(b_min), int(b_max)

    # part 1
    if b_min <= a_min and b_max >= a_max or b_min >= a_min and b_max <= a_max:
        res_1 += 1

    # part 2
    if (
        a_min <= b_min <= a_max
        or a_min <= b_max <= a_max
        or b_min <= a_min <= b_max
        or b_min <= a_max <= b_max
    ):
        res_2 += 1

print(f"Answer 1: {res_1}")
print(f"Answer 2: {res_2}")
