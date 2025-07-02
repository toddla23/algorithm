import sys

input = sys.stdin.readline

n = int(input())
tree = {}
for i in range(1, n + 1):
    tree[i] = []

for _ in range(n-1):
    n, m = map(int, input().split(" "))
    tree[m].append(n)
    tree[n].append(m)

    
print(tree)
