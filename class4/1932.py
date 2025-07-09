import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split(" "))))

# print(arr)

answers = [arr[0].copy()]
for i in range(1, n):
    temp = []
    for j in range(len(arr[i])):
        # print(i, j)
        if j == len(arr[i]) - 1:
            temp.append(arr[i][j] + answers[i - 1][-1])
        elif j == 0:
            temp.append(arr[i][j] + answers[i - 1][0])
        else:
            temp.append(arr[i][j] + max(answers[i - 1][j], answers[i - 1][j - 1]))
        # print(temp)

    answers.append(temp)
print(max(answers[-1]))
