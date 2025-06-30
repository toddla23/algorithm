N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]


tets = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # I
        [(0,1), (1,0), (1,1)], # O
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # Z
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # S
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # L
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # J
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # T
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]

def calc(i,j,tet) :
    temp = arr[i][j] 
    for di,dj in tet :
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0<= nj < M :
            temp += arr[ni][nj]
        else :
            return 0
    return temp


ans = 0
for i in range (N) :
    for j in range (M) :
        for tet in tets:
            temp = calc(i,j,tet)
            ans = max(temp, ans)

print(ans)