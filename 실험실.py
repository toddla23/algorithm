from itertools import combinations

def iterate_three_coords(n, m):
    coords = [(i, j) for i in range(n) for j in range(m)]
    
    for (x1, y1), (x2, y2), (x3, y3) in combinations(coords, 3):
        print((x1, y1), (x2, y2), (x3, y3))

# 예시
iterate_three_coords(2, 3)