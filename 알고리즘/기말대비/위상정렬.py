import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())

    graph = [[]for _ in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(1,n+1):
        temp = list(map(int,input().split()))
        for j in temp[2:]:
            indegree[j]+=1
            graph[i].append(j)
            
            
    toVisit = deque([])
    for i in range(1,n+1):
        if indegree[i] == 0:
            toVisit.append(i)

    result = []
    while toVisit:
        now = toVisit.popleft()
        result.append(now)
        for toGo in graph[now]:
            indegree[toGo] -=1
            if(indegree[toGo] == 0):
                toVisit.append(toGo)


    # for i in graph:
    #     print(i)
        
    # print(indegree)
    if len(result) == n:
        print(" ".join(list(map(str,result))))
    else:
        print(-1)