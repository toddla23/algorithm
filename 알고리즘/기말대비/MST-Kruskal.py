import sys

input = sys.stdin.readline


def union(x, y, parent):
    rx = find(x, parent)
    ry = find(y, parent)

    if rx < ry:
        parent[ry] = rx
    else:
        parent[rx] = ry

    return parent[rx]


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def kruskal(graph, parent):
    cost = 0
    for weight, start, end in graph:
        rStart = find(start, parent)
        rEnd = find(end, parent)
        if rStart == rEnd:
            continue
        union(rStart, rEnd, parent)
        cost += weight
    return cost


n = int(input())
arr = []
union_parent = [i for i in range(n + 1)]

for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    for j in range(2, len(temp), 2):
        arr.append([temp[j + 1], temp[0], temp[j]])  # (weight, start, end)


arr.sort(key=lambda x: x[0])

result = kruskal(arr, union_parent)
print(result)
