import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, isVisit):


n = int(input())

isVisit = [False] * (n+1)
graph = {}
for i in range(1,n+1):
    temp = list(map(int,input().split(" ")))
    graph[i] = temp[2:]


