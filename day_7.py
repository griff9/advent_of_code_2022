class Node:
    def __init__(self, parent=None) -> None:
        self.size = 0
        self.children = {}
        self.parent = parent


with open("advent_of_code\inputs\input_7.txt", "r") as file:
    data = file.read()
data = data.split("\n")
list_1 = []
total_2 = float("inf")


def dfs(n: "Node", target_2: int = 0):
    if not n:
        return 0

    global total_2
    space = n.size
    for child in n.children.values():
        space += dfs(child, target_2)
    if not target_2 and space <= 100000:
        list_1.append(space)
    elif target_2 and total_2 > space >= target_2:
        total_2 = space
    return space


node = root = Node()
for row in data:
    vals = row.split()
    if "$ cd .." in row:
        node = node.parent
    elif "$ cd " in row:
        node = node.children[vals[-1]]
    elif "dir" in row:
        node.children[vals[-1]] = Node(node)
    elif vals and "$" not in row:
        node.size += int(vals[0])

root_space = dfs(root)
needs_space = 30000000 - (70000000 - root_space)
dfs(root, needs_space)

print(f"Answer 1: {sum(list_1)}")
print(f"Answer 2: {total_2}")
