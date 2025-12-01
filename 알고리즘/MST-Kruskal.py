import sys

input = sys.stdin.readline


def ufUion(x, y):
    global union_parent
    rx = ufFind(x)
    ry = ufFind(y)
    if rx < ry:
        union_parent[ry] = rx
    else:
        union_parent[rx] = ry

    return 0


def ufFind(n):
    global union_parent
    if union_parent[n] != n:
        union_parent[n] = ufFind(union_parent[n])
    return union_parent[n]


def kruskal(G):
    mst = []
    cost = 0
    for weight, start, end in G:
        if ufFind(start) != ufFind(end):
            mst.append([weight, start, end])
            ufUion(start, end)
            cost += weight
            
    # for i in mst:
    #     print(i)
    return cost


t = int(input())
for _ in range(t):

    n = int(input())
    arr = []
    union_size = [1] * (n + 1)
    union_parent = [i for i in range(n + 1)]

    for i in range(n):
        temp = list(map(int, input().rstrip().split()))
        for j in range(2, len(temp), 2):
            arr.append([temp[j + 1], temp[0], temp[j]])


    arr.sort(key=lambda x: x[0])

    result = kruskal(arr)
    print(result)