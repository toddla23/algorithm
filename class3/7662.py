import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    heap = []
    isBreak = False
    for _ in range(k):
        calc, n = input().rstrip().split(" ")
        n = int(n)
        if calc == 'I':
            heapq.heappush(heap, n)
        if(len(heap) != 0):
            if calc == 'D' and n == -1:
                heapq.heappop(heap)
            if calc == 'D' and n == 1:
                heap.pop()
        # print(heap)
    
    if(len(heap) == 0):
        print('EMPTY')
    else:
        print(heap[-1], heap[0])
        