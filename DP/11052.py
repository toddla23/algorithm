n = int(input())
priceArr = list(map(int, input().split(" ")))

answerArr = [0 for i in range(n+1)]
for i in range(1, n+1):
  tempArr = []
  for j in range(i):
    tempArr.append(answerArr[j] + priceArr[i - j - 1])
  answerArr[i] = max(tempArr)
print(answerArr[-1])
