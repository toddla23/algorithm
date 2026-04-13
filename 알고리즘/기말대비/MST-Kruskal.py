import sys

input = sys.stdin.readline


def find(x, union_parent):
    if union_parent[x] != x:
        union_parent[x] = find(union_parent[x], union_parent)
    return union_parent[x]


def union(x, y, union_parent):
    rx = find(x, union_parent)
    ry = find(y, union_parent)
    if rx < ry:
        union_parent[ry] = rx
    else:
        union_parent[rx] = ry

    return union_parent[rx]


def kruskal(edges, union_parent):
    answer = 0
    for cost, x, y in edges:
        rx = find(x, union_parent)
        ry = find(y, union_parent)

        if rx == ry:
            continue
        answer += cost
        union(rx, ry, union_parent)
    
    return answer

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    union_parent = [i for i in range(n + 1)]

    for i in range(n):
        temp = list(map(int, input().rstrip().split()))
        for j in range(2, len(temp), 2):
            arr.append([temp[j + 1], temp[0], temp[j]])  # (weight, start, end)


    arr.sort(key=lambda x: x[0])

    print(kruskal(arr, union_parent))
