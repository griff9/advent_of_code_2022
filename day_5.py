import copy

with open("inputs\input_5.txt", "r") as file:
    data = file.read()
data = data.split('\n')

crates = [['empty'] for _ in range(9)]

for r in data[7::-1]:
    
    r = [char for char in r[1::4] ]
    for i,val in enumerate(r):
        if val!= ' ':
            crates[i].append(val)

############################# Part 1
crates_1 = copy.deepcopy(crates)
for r in data[10:]:
     _,amount,__,start,___,end= r.split()
     amount = int(amount)
     start = int(start) - 1
     end = int(end) - 1
     for i in range(amount):
        crates_1[end].append(crates_1[start].pop())

res = ''.join([c[-1] for c in crates_1])

print(f'Answer 1: {res}')

############################# Part 2
for r in data[10:]:
    _,amount,__,start,___,end= r.split()
    amount = int(amount)
    start = int(start) - 1
    end = int(end) - 1
    temp = []
    for i in range(amount):
       temp.append(crates[start].pop())
    temp.reverse()
    crates[end].extend(temp)

res = ''.join([c[-1] for c in crates])

print(f'Answer 2: {res}')
