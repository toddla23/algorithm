def matrixout(mx, size):
    for i in range(size):
        print(mx[i])


# 전치행렬
def transposeMatrix(m):
    return [[m[i][j] for i in range(len(m[j]))] for j in range(len(m))]


# 소행렬 구하기
def getMatrixMinor(m, i, j):
    return [k[:j] + k[j + 1 :] for k in m[:i] + m[i + 1 :]]


# 행렬식 계산
def getMatrixDeterminant(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    for i in range(len(m[0])):
        det += ((-1) ** (i)) * m[0][i] * getMatrixDeterminant(getMatrixMinor(m, 0, i))
    return det


# 역행렬 계산
def getMatrixInverse(m):

    determinant = getMatrixDeterminant(m)

    A = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m[i])):
            temp.append(
                ((-1) ** (i + j)) * getMatrixDeterminant(getMatrixMinor(m, i, j))
            )
        A.append(temp)
    matrixout(A, 3)

    t = transposeMatrix(A)
    matrixout(t, 3)
    return [[j / determinant for j in i] for i in t]


m0 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
m1 = [[4, 3], [3, 2]]
print(getMatrixDeterminant(m0))
matrixout(getMatrixInverse(m0), 3)
# matrixout()
