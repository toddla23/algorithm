import sys
import copy

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split(" "))))
    
minArr = copy.deepcopy(arr[0])
maxArr = copy.deepcopy(arr[0])

for i in range(1, n):
    prev_max = maxArr[:]
    prev_min = minArr[:]

    maxArr[0] = max(prev_max[0], prev_max[1]) + arr[i][0]
    maxArr[1] = max(prev_max[0], prev_max[1], prev_max[2]) + arr[i][1]
    maxArr[2] = max(prev_max[1], prev_max[2]) + arr[i][2]

    minArr[0] = min(prev_min[0], prev_min[1]) + arr[i][0]
    minArr[1] = min(prev_min[0], prev_min[1], prev_min[2]) + arr[i][1]
    minArr[2] = min(prev_min[1], prev_min[2]) + arr[i][2]


print(max(maxArr), min(minArr))