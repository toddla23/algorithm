import sys

n, m = map(int, input().split(" "))

dic = {}
for _ in range(n):
    site, password = sys.stdin.readline().strip().split(" ")
    dic[site] = password

for _ in range(m):
    print(dic[sys.stdin.readline().strip()])
