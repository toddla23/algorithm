import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t = int(input())
    arr.append(t)
    
arr.sort()
maxValue = 0
for i in range(n):
    maxValue = max(maxValue, (n-i)*arr[i])
    
print(maxValue)
    