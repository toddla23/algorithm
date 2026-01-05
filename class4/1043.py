def u_find(x, parent):
    if x != parent[x]:
        parent[x] = u_find(parent[x], parent)
    return parent[x]


def u_union(x, y, parent, member):
    rx = u_find(x, parent)
    ry = u_find(y, parent)

    if member[parent[rx]]:
        parent[ry] = parent[rx]
    elif member[parent[ry]]:
        parent[rx] = parent[ry]
    else:
        parent[rx] = parent[ry]

    return


n, m = list(map(int, input().split()))
T_party = list(map(int, input().split()))
T_party = T_party[1:]

member = [False for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
for i in T_party:
    member[i] = True

arr = []
for _ in range(m):
    t = list(map(int, input().split()))
    arr.append(t[1:])

# print(member)

for i in arr:
    # print(i)
    for j in range(1, len(i)):
        u_union(i[0], i[j], parent, member)

    # print(parent)

answer = 0
for i in arr:
    temp = False
    for j in i:
        temp = temp or member[u_find(j, parent)]
    if not temp:
        answer += 1

print(answer)
