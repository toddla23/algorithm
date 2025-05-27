def getAnswer(graph: dict, addr: int):
    answer.add(addr)
    if addr in graph.keys():
        # print(f"addr: {addr}, value: {graph[addr]}")
        for i in graph[addr]:
            if i not in answer:
                getAnswer(graph=graph, addr=i)
    else:
        return


n = int(input())

answer = set()
graph = {}
k = int(input())
for _ in range(k):
    a, b = map(int, input().split(" "))
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

# print(graph)
if n == 0 or k == 0:
    print(0)
else:
    for i in graph[1]:
        getAnswer(graph=graph, addr=i)
    # print(answer)
    answer.discard(1)
    print(len(answer))
