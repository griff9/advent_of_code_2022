from collections import deque
import heapq
import math
import re


class Monkey:
    def __init__(self, num, items, op, test, t_monkey, f_monkey) -> None:
        self.num = num
        self.items = [int(val) for val in items]
        self.cnt = 0
        self.op, self.amount = op.split()[-2], op.split()[-1]
        self.test = test
        self.t_monkey = t_monkey
        self.f_monkey = f_monkey


with open("inputs\input_test.txt", "r") as file:
    data = file.read()
data = deque(data.split("\n"))
monos = []

while data:
    num = int(re.findall("\d", data.popleft())[0])
    items = re.findall("\d+", data.popleft())
    op = data.popleft()
    test = int(re.findall("\d+", data.popleft())[0])
    t_monkey = int(re.findall("\d+", data.popleft())[0])
    f_monkey = int(re.findall("\d+", data.popleft())[0])
    monos.append(Monkey(num, items, op, test, t_monkey, f_monkey))
    if data:
        data.popleft()


def monkey_business(rounds, lcm) -> int:
    for rnd in range(rounds):
        for m in monos:
            for i in m.items:
                amount = int(m.amount) if m.amount != "old" else i
                i = (i * amount) % lcm if m.op == "*" else (i + amount) % lcm
                if i % m.test != 0:
                    monos[m.f_monkey].items.append(i)
                else:
                    monos[m.t_monkey].items.append(i)
            m.cnt += len(m.items)
            m.items = []

    top_2 = heapq.nlargest(2, monos, key=lambda x: x.cnt)
    #print(top_2[0].cnt,top_2[1].cnt)
    return top_2[0].cnt * top_2[1].cnt

#I broke answer 1 somehow and need to fix it later
#print(f'Answer 1: {monkey_business(20,3)}')
print(f"Answer 2: {monkey_business(10000,math.lcm(3,5,2,13,11,17,19,7))}") #hard coded the divisibles as lcm was complaining about taking an iterable
