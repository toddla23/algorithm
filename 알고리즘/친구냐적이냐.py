import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    if a == -1: return b
    if b == -1: return a
    ra = find(a, parent)
    rb = find(b, parent)
    if ra == rb: return ra
    parent[rb] = ra
    return ra

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    enemy = [-1] * n

    for _ in range(m):
        q, x, y = map(int, input().split())
        rx = find(x, parent)
        ry = find(y, parent)

        if q == 1:    
            if enemy[rx] == ry:
                print(0)
                continue

            r = union(rx, ry, parent)
            e = union(enemy[rx], enemy[ry], parent)
            enemy[r] = e
            if e != -1:
                enemy[e] = r

        elif q == 2:  
            if rx == ry:
                print(0)
                continue

            ex = enemy[rx]
            ey = enemy[ry]

            nrx = union(ex, ry, parent)
            nry = union(ey, rx, parent)

            enemy[nrx] = nry
            enemy[nry] = nrx

        else:         
            if rx == ry:
                print(1)  
            elif enemy[rx] == ry:
                print(2)  
            else:
                print(3) 
