import sys

n, m = map(int, input().split(" "))

see = set()
for _ in range(n):
    see.add(sys.stdin.readline().strip())

hear = set()
for _ in range(m):
    hear.add(sys.stdin.readline().strip())

answer = list(see.intersection(hear))
answer.sort()
print(len(answer))
for i in list(answer):
    print(i)
