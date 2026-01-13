import sys
sys.setrecursionlimit(1000000)



def calc(start, arr, visited):
    # print(start)
    longR = 0
    visited[start] = True
    x = start
    for i in range(len(arr[start])):
        a, cost = arr[start][i]
        if visited[a]:
            continue
        s, c = calc(a, arr, visited)
        if longR < c+cost:
            longR = c + cost
            x = s

    return (x, longR)


n = int(input())


arr = [[] for _ in range(n + 1)]


for _ in range(n - 1):
    r, k, c = list(map(int, input().split()))
    arr[r].append((k, c))
    arr[k].append((r, c))

# for i in arr:
#     print(i)

s, c = calc(1, arr, [False] * (n + 1))
t, answer = calc(s,arr,[False] * (n + 1))
print(answer)

