import heapq
import sys

input = sys.stdin.readline

n = int(input())

max_heap = []

for _ in range(n):
    a = int(input())
    if a == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap) * -1)
    else:
        heapq.heappush(max_heap, -1 * a)
