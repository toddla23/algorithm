import sys

input = sys.stdin.readline


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, union):
    if x > y:
        union[x] = union[y]
    else:
        union[y] = union[x]
    return


n, m = list(map(int, input().split(" ")))
friend = [i for i in range(n)]
enemy = [-1 for _ in range(n)]

for i in range(m):
    q, x, y = list(map(int, input().split(" ")))
    rx = find(x, friend)
    ry = find(y, friend)
    if q == 1:
        if friend[x] == friend[y]:
            print(0)
            continue
        union(rx, ry, friend) # 친구 맺기
        union(enemy[rx], enemy[ry], friend) # 적의 적은 찬구

    elif q == 2:
        if rx == ry:
            print(0)
            continue
        
        ex = enemy[rx]
        ey = enemy[ey]
