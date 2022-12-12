from collections import deque


def travel(all: bool = False):
    with open("inputs\input_12.txt", "r") as file:
        data = file.read()
    grid = [list(row) for row in data.split("\n")]
    M, N = len(grid), len(grid[0])
    q, visited = deque(), set()
    for r in range(M):
        for c in range(N):
            if grid[r][c] == "S" or (all and grid[r][c] == "a"):
                q.append((r, c, 1))
                visited.add((r, c))
                grid[r][c] = "a"
            elif grid[r][c] == "E":
                end = (r, c)
                grid[r][c] = "z"

    while q:
        r, c, cnt = q.popleft()

        for R, C in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
            if (
                0 <= R < M
                and 0 <= C < N
                and (R, C) not in visited
                and (ord(grid[r][c]) + 1 >= ord(grid[R][C]))
            ):
                if (R, C) == end:
                    return cnt
                q.append((R, C, cnt + 1))
                visited.add((R, C))
    return -1


print(f"Answer 1: {travel()}")
print(f"Answer 2: {travel(True)}")
