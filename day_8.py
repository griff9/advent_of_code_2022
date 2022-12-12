from collections import deque


with open("inputs\input_8.txt", "r") as file:
    data = file.read()
grid = [[int(col) for col in row] for row in data.split("\n")]
M, N = len(grid), len(grid[0])

############################# Part 1
visited = set()

# left,right
for first_c, start, end, step_size in (0, 1, N - 1, 1), (M - 1, N - 2, 0, -1):
    for r in range(1, M - 1):
        tall = grid[r][first_c]
        for c in range(start, end, step_size):
            if grid[r][c] > tall:
                visited.add((r, c))
                tall = grid[r][c]

# up,down
for first_r, start, end, step_size in (0, 1, M - 1, 1), (N - 1, N - 2, 0, -1):
    for c in range(1, N - 1):
        tall = grid[first_r][c]
        for r in range(start, end, step_size):
            if grid[r][c] > tall:
                visited.add((r, c))
                tall = grid[r][c]

print(f"Answer 1: {len(visited) + 2*M + 2*N - 4}")


############################# Part 2
res = 0
for r in range(1, M - 1):
    for c in range(1, N - 1):
        height = grid[r][c]
        n = e = s = w = 1
        while r + e < N - 1 and grid[r + e][c] < height:
            e += 1
        while r - w > 0 and grid[r - w][c] < height:
            w += 1
        while c + s < M - 1 and grid[r][c + s] < height:
            s += 1
        while c - n > 0 and grid[r][c - n] < height:
            n += 1
        res = max(res, n * s * w * e)

print(f"Answer 2: {res}")

####### Need to refactor to a monostack at some point. Part 2 here has terrible time complexity the below is work in progress
"""
scores = [[0 for _ in range(N)] for _ in range(M)]
for r in range(M):
    stack = deque()
    stack.append([float('inf'),1])
    for c in range(N):
        #if r==3: print('top',grid[r][c])
        while grid[r][c]>stack[-1][0]:
            #if r==3: print('popping',stack)
            scores[r][c]+=stack[-1][1]
            stack.pop()
        else:
            stack.append([grid[r][c],1 + scores[r][c]])
            scores[r][c] += 1 if len(stack) > 2 else 0

#print(scores)

for r in range(M):
    stack = deque()
    stack.append([float('inf'),1])
    for c in range(N-1,-1,-1):
        #if r==3: print('top',grid[r][c])
        while grid[r][c]>stack[-1][0]:
            #if r==3: print('popping',stack)
            scores[r][c]+=stack[-1][1]
            stack.pop()
        else:
            stack.append([grid[r][c],1 + scores[r][c]])
            scores[r][c] += 1 if len(stack) > 2 else 0

#print(scores)"""
