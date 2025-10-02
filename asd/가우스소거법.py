def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        # 1. 피벗 선택 (0이면 아래 행과 교환)
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break

        # 2. 피벗을 1로 만들기
        pivot = matrix[i][i]
        matrix[i] = [x / pivot for x in matrix[i]]
        # print(matrix)

        # 3. 피벗 아래를 0으로 만들기
        for j in range(i + 1, n):
            factor = matrix[j][i]
            matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]

    # 4. 뒤에서부터 위쪽을 0으로 만들기 (역대입)
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]
        print(matrix)

    # 해 벡터 추출
    return [row[-1] for row in matrix]


# 예시: x + y + z = 6, 2y + 5z = -4, 2x + 5y - z = 27
A = [
    [1, 1, 1, 6],
    [0, 2, 5, -4],
    [2, 5, -1, 27]
]

solution = gaussian_elimination(A)
print("해:", solution)  # [5.0, 3.0, -2.0]
