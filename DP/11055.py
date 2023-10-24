t = int(input())

arr = list(map(int, input().split(" ")))

answerArr = [i for i in arr]
for i in range(t):
  temp = 0
  for j in range(i):
    # print('arr[i]' , arr[i],'arr[j]', arr[j])
    if (arr[i] > arr[j] and temp < answerArr[j]):
      temp = answerArr[j]
  answerArr[i] = answerArr[i] + temp
print(max(answerArr))

