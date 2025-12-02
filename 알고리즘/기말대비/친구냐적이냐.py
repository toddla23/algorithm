def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x,y,parent):
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
        if enemy[rx] == ry:
            print(0)
            continue
        
        r = union(rx, ry, parent) # 두 친구 그룹 결합한 친구 루트
        e = union(enemy[rx], enemy[ry], parent) # 두 적 그룹 결합한 적 루트
        enemy[r] = e # 친구 루트의 적은 적 루트
        if e == -1: # 적
            enemy[e] = r
        
        
