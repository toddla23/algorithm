import sys
from decimal import Decimal

input = sys.stdin.readline

explainNeed = False


# 행렬 프린트
def printMatrix(matrix):
    for i in matrix:
        print(i)


# 전치행렬
def getTransposeMatrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]


# 소행렬
def getMinorMatrix(matrix, x, y):
    return [i[:x] + i[x + 1 :] for i in matrix[:y] + matrix[y + 1 :]]


# 2*2 행렬식 계산
def get2By2Determinent(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


# 행렬식 계산
def getDetrminent(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return get2By2Determinent(matrix)

    result = 0
    for i in range(len(matrix[0])):
        result = result + matrix[0][i] * getConfector(matrix, i, 0)
    return result


# 여인수 계산
def getConfector(matrix, x, y):
    return (-1) ** (x + y) * getDetrminent(getMinorMatrix(matrix, x, y))


# 역행렬
def getInverseMatrix(matrix):
    global explainNeed
    determinent = getDetrminent(matrix)
    if explainNeed:
        print(f"행렬식: {determinent}")

    result = []
    for y in range(len(matrix)):
        temp = []
        for x in range(len(matrix[y])):
            temp.append(getConfector(matrix, x, y))
        result.append(temp)
    if explainNeed:
        print("여인수 행렬")
        printMatrix(result)

    t = getTransposeMatrix(result)
    if explainNeed:
        print("여인수 행렬의 전치행렬")
        printMatrix(t)

    return [[j / determinent for j in i] for i in t]
    # return [[f"{j} / {determinent}" for j in i] for i in t]


# 단위행렬
def getUnitMatrix(size):
    unitMatix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        unitMatix[i][i] = 1
    return unitMatix


# 가우스 조던 소거법
def GaussJordanElimination(matrix):
    global explainNeed
    unitMatix = getUnitMatrix(len(matrix))

    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            temp1 = matrix[i][i]
            for k in range(len(matrix[i])):
                matrix[i][k] = matrix[i][k] / temp1
                unitMatix[i][k] = unitMatix[i][k] / temp1

        for j in range(i + 1, len(matrix)):
            temp2 = matrix[j][i]
            for k in range(len(matrix[j])):
                matrix[j][k] = matrix[j][k] - (temp2 * matrix[i][k])
                unitMatix[j][k] = unitMatix[j][k] - (temp2 * unitMatix[i][k])
        printMatrix(matrix)
        printMatrix(unitMatix)
            # print(f"i:{i}, j:{j}, k:{k}, result: {matrix[j][k] - (matrix[j][i] * matrix[i][k])}")
    if explainNeed:
        print("가우스 소거법 결과")
        print("원본 행렬")
        printMatrix(matrix)
        print("단위행렬")
        printMatrix(unitMatix)

    for i in range(len(matrix) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            temp = matrix[j][i]
            for k in range(len(matrix[j])):
                matrix[j][k] = matrix[j][k] - (temp * matrix[i][k])
                unitMatix[j][k] = unitMatix[j][k] - (temp * unitMatix[i][k])

    return unitMatix


def main():
    global explainNeed
    try:
        print("정방행렬의 차수 입력")
        n = int(input())
        if n <= 0:
            print("차수는 양의 정수여야 합니다.")
        matrix = []
        print(f"{n}*{n} 정방 행렬 입력 (공백으로 구분하여 한줄씩)")
        for _ in range(n):
            try:
                matrix.append(list(map(int, input().split(" "))))
            except:
                print("입력오류")
        print(matrix)
        determinent = getDetrminent(matrix)
        if determinent == 0:
            print("헹렬식이 0이므로 역행렬을 구할 수 없습니다.")
            return
        
        print("각 행렬식을 구하는 과정이 필요한가요? 1.예 2. 아니요")
        if int(input()) == 1:
            explainNeed = True

        print("1. 행렬식을 이용한 역행렬")
        result1 = getInverseMatrix(matrix)
        print("결과:")
        printMatrix(result1)
        print("----------------------------------------------------------------")
        print("2. 가우스-조던 소거법(Gauss-Jordan elimination)을 이용한 역행렬")
        result2 = GaussJordanElimination(matrix)
        print("결과:")
        printMatrix(result2)

        valid = True
        for i in range(n):
            if valid == False:
                break
            for j in range(n):
                if result1[i][j] != result2[i][j]:
                    valid = False
                    break
        print("일치합니다" if valid else "일치하지 않습니다")
    except ValueError:
        print("입력 오류! 정수가 아닙니다.")
    # except Exception as e:
    #     print("예상치 못한 오류 발생")
    # matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]


main()
