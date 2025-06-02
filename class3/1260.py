dfs_answer = []
bfs_answer = []


def dfs(graph: dict, start: int):
    dfs_answer.append(start)
    # print(dfs_answer)
    if start not in graph.keys():
        return
    for i in graph[start]:
        if i not in dfs_answer:
            dfs(graph=graph, start=i)


temp = []


def bfs(graph: dict, start: int):
    temp.append(start)
    while temp:
        addr = temp.pop(0)
        for i in graph[addr]:
            if i not in bfs_answer and i not in temp:
                temp.append(i)
        bfs_answer.append(addr)
        # print(f"start: {start}")
        # print(f"bfs_answer: {bfs_answer}")
        # print(f"temp:{temp}")


n, m, v = map(int, input().split(" "))

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split(" "))
    if a in graph.keys():
        graph[a].append(b)
        graph[a].sort()
    else:
        graph[a] = [b]
    if b in graph.keys():
        graph[b].append(a)
        graph[b].sort()
    else:
        graph[b] = [a]


# print(graph)

dfs(graph=graph, start=v)

bfs(graph=graph, start=v)

print(*dfs_answer)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(*bfs_answer)
