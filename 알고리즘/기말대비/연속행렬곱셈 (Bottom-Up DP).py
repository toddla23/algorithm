INF = float("inf")

def calc(a, b, locations):
    # print(a,b)
    if a == b:
        return ""
    if a + 1 == b:
        return f"M{a+1}"

    return f"({    calc(a, locations[a][b], locations)}{    calc(locations[a][b], b, locations)})"

t = int(input())
for _ in range(t):
    n = int(input()) + 1

    arr = list(map(int, input().split()))

    answers = [[0] * n for _ in range(n)]
    locations = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(0, n - length):
            j = i + length
            minAnswer = INF
            location = 0
            for k in range(i + 1, j):
                answer = answers[i][k] + answers[k][j] + (arr[i] * arr[k] * arr[j])
                if answer < minAnswer:
                    minAnswer = answer
                    location = k
            answers[i][j] = minAnswer
            locations[i][j] = location

    print(calc(0, n - 1, locations))
    print(answers[0][-1])

