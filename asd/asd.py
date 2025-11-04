from decimal import Decimal, getcontext
import sys

input = sys.stdin.readline
getcontext().prec = 30  # 소수점 30자리 정밀도

explainNeed = False


def printMatrix(matrix):
    for row in matrix:
        print([float(x) for x in row])


# 전치행렬
def getTransposeMatrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]


# 소행렬
def getMinorMatrix(matrix, x, y):
    return [row[:x] + row[x + 1 :] for row in matrix[:y] + matrix[y + 1 :]]


# 2*2행렬식 계산
def get2By2Determinent(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


# 행렬식 계산
def getDetrminent(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return get2By2Determinent(matrix)

    result = Decimal(0)
    for i in range(len(matrix[0])):
        result += matrix[0][i] * getConfector(matrix, i, 0)
    return result


# 여인수 계산
def getConfector(matrix, x, y):
    return Decimal((-1) ** (x + y)) * getDetrminent(getMinorMatrix(matrix, x, y))


# 역행렬 계산
def getInverseMatrix(matrix):
    global explainNeed
    det = getDetrminent(matrix)

    if det == 0:
        print("[오류] 행렬식이 0이므로 여인수를 이용한 역행렬을 구할 수 없습니다.")
        return None

    if explainNeed:
        print(f"행렬식: {det}")

    cofactors = []
    for y in range(len(matrix)):
        row = []
        for x in range(len(matrix[y])):
            row.append(getConfector(matrix, x, y))
        cofactors.append(row)
    if explainNeed:
        print("여인수 행렬")
        printMatrix(cofactors)

    adjugate = getTransposeMatrix(cofactors)
    if explainNeed:
        print("전치 행렬:")
        printMatrix(adjugate)

    return [
        [adjugate[i][j] / det for j in range(len(adjugate[i]))]
        for i in range(len(adjugate))
    ]


# 단위행렬
def getUnitMatrix(size):
    unit = [[Decimal(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        unit[i][i] = Decimal(1)
    return unit


def GaussJordanElimination(matrix):
    global explainNeed

    det = getDetrminent(matrix)
    if det == 0:
        print(
            "[오류] 행렬식이 0이므로 가우스-조던 소거법으로 역행렬을 구할 수 없습니다."
        )
        return None

    n = len(matrix)
    unit = getUnitMatrix(n)

    for i in range(n):
        pivot = matrix[i][i]
        if pivot != 1:
            for k in range(n):
                matrix[i][k] /= pivot
                unit[i][k] /= pivot

        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= factor * matrix[i][k]
                unit[j][k] -= factor * unit[i][k]

    if explainNeed:
        print("가우스 소거법 결과")
        print("원본 행렬")
        printMatrix(matrix)
        print("단위행렬")
        printMatrix(unit)

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= factor * matrix[i][k]
                unit[j][k] -= factor * unit[i][k]

    return unit


def main():
    global explainNeed
    print("정방행렬의 차수 입력")
    n = int(input())
    if n <= 0:
        print("차수는 양의 정수여야 합니다.")
        return

    print(f"{n}*{n} 정방 행렬 입력 (공백으로 구분하여 한줄씩)")
    matrix = []
    for _ in range(n):
        matrix.append([Decimal(x) for x in input().split()])

    print("각 행렬식을 구하는 요소가 필요한가요? 1.예 2. 아니요")
    if int(input()) == 1:
        explainNeed = True

    print("1. 행렬식을 이용한 역행렬")
    result1 = getInverseMatrix(matrix)
    if result1 is not None:
        print("결과:")
        printMatrix(result1)

    print("2. 가우스-조던 소거법으로 구한 역행렬")
    matrix_copy = [row[:] for row in matrix]
    result2 = GaussJordanElimination(matrix_copy)
    if result2 is not None:
        print("결과:")
        printMatrix(result2)

    if result1 is not None and result2 is not None:
        same = all(
            all(abs(result1[i][j] - result2[i][j]) < Decimal("1e-20") for j in range(n))
            for i in range(n)
        )
        print("결과 일치" if same else "결과 불일치")


main()
