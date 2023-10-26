t = int(input())
arr = list(map(int, input().split(" ")))

upAnswerArr = [1 for i in range(t)]
downAnswerArr = [1 for i in range(t)]

for i in range(1, t):
  for j in range(i):
    if(arr[i] > arr[j] and upAnswerArr[i] <= upAnswerArr[j]):
      upAnswerArr[i] = upAnswerArr[j] + 1

for i in range(t, -1, -1):
  for j in range(i, t):
    if(arr[i] > arr[j] and downAnswerArr[i] <= downAnswerArr[j]):
      downAnswerArr[i] = downAnswerArr[j] + 1

answerArr = []
for i in range(t):
  answerArr.append(downAnswerArr[i] + upAnswerArr[i] - 1)
print(max(answerArr))