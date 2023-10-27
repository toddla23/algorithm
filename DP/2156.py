t = int(input())
arr = []

for i in range(t):
  arr.append(int(input()))

answerArr = [[0 for i in range(t)] for i in range(3)]


answerArr[1][0] = arr[0]
answerArr[2][0] = arr[0]

for i in range(1, t):
  answerArr[0][i] = max(answerArr[1][i-1], answerArr[2][i-1], answerArr[0][i-1])
  answerArr[1][i] = answerArr[0][i-1] + arr[i]
  answerArr[2][i] = answerArr[1][i-1] + arr[i]

# print(answerArr)
print(max(answerArr[0][t-1], answerArr[1][t-1], answerArr[2][t-1]))