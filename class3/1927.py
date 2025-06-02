import heapq
import sys

min_heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(int(sys.stdin.readline()))
    if n > 0:
        heapq.heappush(min_heap, n)
    else:
        if len(min_heap) == 0:
            print(0)
        else:
            a = heapq.heappop(min_heap)
            print(a)
    # print(min_heap)
