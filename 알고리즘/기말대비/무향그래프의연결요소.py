import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, graph, isVisit):
    toVisits = deque([x])
    count = 0
    while toVisits:
        toVisit = toVisits.popleft()
        if isVisit[toVisit]:
            continue
        isVisit[toVisit] = True
        count += 1
        for i in graph[toVisit]:
            if not isVisit[i]:
                toVisits.append(i)

    return count

t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    isVisit = [False for _ in range(n + 1)]
    for _ in range(n):
        temp = list(map(int, input().rstrip().split()))
        u = temp[0]
        v = temp[1]
        
        dic[temp[0]] = temp[2:2+v]
    answer = []
    for i in range(1, n + 1):
        if not isVisit[i]:
            answer.append(bfs(i, dic, isVisit))
            
    answer.sort()
    print(len(answer), " ".join(list(map(str,answer))))
    
