import sys
input = sys.stdin.readline

INF = float('inf')

H = [None]
xmap = {}

def LeftChild(i): return 2*i
def RightChild(i): return 2*i+1
def Parent(i): return i//2

def SwapHeap(i, j):
    H[i], H[j] = H[j], H[i]
    xmap[H[i][0]] = i
    xmap[H[j][0]] = j

def Heapify(i):
    smallest = i
    left = LeftChild(i)
    right = RightChild(i)
    size = len(H) - 1

    if left <= size and H[left][1] < H[smallest][1]:
        smallest = left
    if right <= size and H[right][1] < H[smallest][1]:
        smallest = right

    if smallest != i:
        SwapHeap(i, smallest)
        Heapify(smallest)

def UpHeap(i):
    while i > 1 and H[Parent(i)][1] > H[i][1]:
        SwapHeap(i, Parent(i))
        i = Parent(i)

def Insert(id, key):
    H.append((id, key))
    idx = len(H) - 1
    xmap[id] = idx
    UpHeap(idx)

def DeleteMin():
    size = len(H) - 1
    if size == 0: return None

    min_elem = H[1]
    SwapHeap(1, size)
    H.pop()
    del xmap[min_elem[0]]

    if len(H) > 1:
        Heapify(1)

    return min_elem

def DecreaseKey(id, new_key):
    i = xmap.get(id)
    if i is None: return
    if new_key >= H[i][1]: return
    H[i] = (id, new_key)
    UpHeap(i)


def MST_Prim(Graph):
    vertices = list(Graph.keys())
    visited = {v: False for v in vertices}
    min_weight = 0

    global H, xmap
    H = [None] + [(v, INF) for v in vertices]
    xmap = {v: i for i, v in enumerate(vertices, start=1)}

    start = vertices[0]
    H[xmap[start]] = (start, 0)
    UpHeap(xmap[start])

    while len(H) > 1:
        v, wt = DeleteMin()
        min_weight += wt
        visited[v] = True

        for nv, nwt in Graph[v]:
            if not visited[nv]:
                idx = xmap.get(nv)
                if idx is None:
                    Insert(nv, nwt)
                else:
                    if nwt < H[idx][1]:
                        DecreaseKey(nv, nwt)

    return min_weight


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    Graph = {i: [] for i in range(1, n+1)}

    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        m = data[1]
        edges = data[2:]

        for i in range(0, 2*m, 2):
            v = edges[i]
            w = edges[i+1]
            Graph[k].append((v, w))

    result = MST_Prim(Graph)
    print(result)
