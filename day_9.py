###################NEEDS Work Still



import math

class Knot:
    def __init__(self,num) -> None:
        self.x = 0
        self.y = 0
        self.num = num
        self.next = None

    def __repr__(self) -> str:
        return f'{self.num}: ({self.x},{self.y})'


with open("inputs\input_9.txt", "r") as file:
    data = file.read()
data = data.split('\n')

visited_1 = [(0,0)]
visited_2 = [(0,0)]
head = current = Knot(0)
temp_lst = [head]
for i in range(1,10):
    current.next = Knot(i)
    current = current.next
    temp_lst.append(current)

for row in data:
    dir,cnt = row.split()
    for i in range(int(cnt)):
        if dir in 'UD':
            head.y += 1 if dir=='U' else -1
        else:
            head.x += 1 if dir=='R' else -1
        current = head
        while current.next:
            H, T = current, current.next
            if current.num==9:print(f'head:({H.x},{H.y})')
            #print('distance:',math.sqrt((H.x - T.x)**2 + (H.y - T.y)**2))
            if math.sqrt((H.x - T.x)**2 + (H.y - T.y)**2)>=2:
                #if current.num==0: print('distance:',math.sqrt((H.x - T.x)**2 + (H.y - T.y)**2))

                diff_x = H.x - T.x
                diff_y = H.y - T.y
                T.x, T.y = H.x, H.y

                if abs(diff_y) > abs(diff_x):
                    T.y-= 1 if diff_y>0 else -1
                elif abs(diff_x) > abs(diff_y):
                    T.x-= 1 if diff_x>0 else -1

                if T.num == 1:    
                    visited_1.append((T.x,T.y))
                if T.num == 3:
                    visited_2.append((T.x,T.y))
                #if current.num==0: print(f'tail:({T.x},{T.y})')
            current = current.next

#show(temp_lst)
visited_1 = set(visited_1)
visited_2 = set(visited_2)

############################# Part 1
print(f'Answer 1: {len(visited_1)}')



############################# Part 2
print(f'Answer 2: {len(visited_2)}')

'''x = Hy = Tx = Ty = 0

for row in data:
    dir,cnt = row.split()
    for i in range(int(cnt)):
        if dir in 'UD':
            Hy += 1 if dir=='U' else -1
        else:
            Hx += 1 if dir=='R' else -1
        #print(f'head:({Hx},{Hy})')
        if math.sqrt((Hx - Tx)**2 + (Hy - Ty)**2)>1.5:
            #print('distance:',math.sqrt((Hx - Tx)**2 + (Hy - Ty)**2))
            if dir == 'U':
                Tx, Ty = Hx, Hy-1
            elif dir =="D":
                Tx, Ty = Hx, Hy+1
            elif dir =="L":
                Tx, Ty = Hx+1, Hy
            elif dir =="R":
                Tx, Ty = Hx-1, Hy
            visited.append((Tx,Ty))
        #print(f'tail:({Tx},{Ty})')
#print(visited)
visited = set(visited)'''