import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split(" "))

arr = [0 for _ in range(101)]
ladder = [0 for _ in range(101)]
for _ in range(n):
    x,y = map(int, input().split(" "))
    ladder[x] = y

for _ in range(m):
    x,y = map(int, input().split(" "))
    ladder[x] = y

toVisit = deque([])
toVisit.append(1)
arr[1]= 1
while arr[100]== 0:
    target = toVisit.popleft()
    for i in range(1, 7):
        toGo = target + i
        if(toGo > 100):
            continue
        
        if(arr[toGo] == 0):
            arr[toGo] = arr[target] + 1
            if(ladder[toGo] == 0):
                toVisit.append(toGo)
            else:
                if(arr[ladder[toGo]] == 0):
                    arr[ladder[toGo]] = arr[target] + 1
                toVisit.append(ladder[toGo])
                
# print(arr)
print(arr[100]-1)
                
        