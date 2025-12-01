n, m = list(map(int, input().split()))


def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents):
    parents[y] = x


parents = [i for i in range(n + 1)]

answer = 0
for i in range(m):
    u, v = list(map(int, input().split()))
    ru = find(u, parents)
    rv = find(v, parents)
    if ru == rv:
        answer = 1
    else:
        union(ru, rv, parents)
print(answer)
