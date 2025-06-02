import sys

input = sys.stdin.readline


def dfs(graph: dict, addr: int):
    global visited
    visited.append(addr)

    for i in graph[addr]:
        if i not in visited:
            dfs(graph=graph, addr=i)


n, m = map(int, input().split(" "))
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split(" "))
    # if u in graph.keys():
    #     graph[u].append(v)
    # else:
    #     graph[u] = [v]
    # if v in graph.keys():
    #     graph[v].append(u)
    # else:
    #     graph[v] = [u]

    graph[u].append(v)
    graph[v].append(u)


visited = []
answer = 0

# print(graph)
for i in graph.keys():
    if i in visited:
        continue
    else:
        dfs(graph=graph, addr=i)
        answer += 1
print(answer)
