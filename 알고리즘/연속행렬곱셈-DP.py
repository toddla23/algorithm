def matrix_chain_order(d):
    n = len(d) - 1  # 행렬 개수
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    # L = 체인 길이 (2부터 n까지)
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def print_paren(split, i, j):
    if i == j:
        return f"M{i}"
    else:
        k = split[i][j]
        left = print_paren(split, i, k)
        right = print_paren(split, k + 1, j)
        return f"({left}{right})"


# 실행 부분
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    d = list(map(int, input().strip().split()))
    dp, split = matrix_chain_order(d)
    formula = print_paren(split, 1, n)
    print(formula)
    print(dp[1][n])
