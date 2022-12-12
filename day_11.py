import heapq
import math
import re


class Monkey:
    def __init__(self, monkey_info) -> None:
        self.num = int(re.findall("\d", monkey_info[0])[0])
        self.items = [int(i) for i in re.findall("\d+", monkey_info[1])]
        self.op = monkey_info[2].split()[-2]
        self.amount = monkey_info[2].split()[-1]
        self.test = int(re.findall("\d+", monkey_info[3])[0])
        self.t_monkey = int(re.findall("\d+", monkey_info[4])[0])
        self.f_monkey = int(re.findall("\d+", monkey_info[5])[0])
        self.cnt = 0


with open("inputs\input_11.txt", "r") as file:
    data = file.read()
data = data.split("\n\n")


def create_monkeys() -> list:
    monos = []
    for monkey in data:
        monos.append(Monkey(monkey.split("\n")))
    return monos


def monkey_business(monos, rounds, lcm=None) -> int:
    for _ in range(rounds):
        for m in monos:
            for i in m.items:
                amount = int(m.amount) if m.amount != "old" else i
                i = (i * amount) if m.op == "*" else (i + amount)
                i = i % lcm if lcm else i // 3
                if i % m.test != 0:
                    monos[m.f_monkey].items.append(i)
                else:
                    monos[m.t_monkey].items.append(i)
            m.cnt += len(m.items)
            m.items = []

    top_2 = heapq.nlargest(2, monos, key=lambda x: x.cnt)
    return top_2[0].cnt * top_2[1].cnt


print(f"Answer 1: {monkey_business(create_monkeys(),20)}")
print(f"Answer 2: {monkey_business(create_monkeys(),10000,math.lcm(3,5,2,13,11,17,19,7))}")
# hard coded the divisibles as lcm was complaining about taking an iterable
