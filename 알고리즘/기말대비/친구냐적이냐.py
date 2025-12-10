def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    if x == -1:
        return y
    if y == -1:
        return x
    
    rx = find(x, parent)
    ry = find(y, parent)
    if rx == ry:
        return rx

    parent[ry] = rx
    return rx


n, m = map(int, input().split())
parent = [i for i in range(n)]
enemy = [-1] * n

for _ in range(m):
    q, x, y = map(int, input().split())
    rx = find(x, parent)
    ry = find(y, parent)

    if q == 1:
        if rx == ry:
            continue
        if enemy[rx] == ry:
            print(0)
            continue
        rf = union(rx, ry, parent)  # 친구 맺기
        re = union(enemy[rx], enemy[ry], parent)  # 적의 적은 친구
        enemy[rf] = re
        if re != -1:
            enemy[re] = rf
            
    elif q == 2:
        if rx == ry:
            print(0)
            continue
        ex = enemy[rx]
        ey = enemy[ry]
        
        
