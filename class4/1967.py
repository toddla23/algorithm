n = int(input())

arr = [[] for _ in range(n + 1)]


for _ in range(n-1):
    r, n, c = list(map(int, input().split()))
    arr[r].append((n,c))

for i in arr:
    print(i)