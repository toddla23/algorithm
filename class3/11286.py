import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
