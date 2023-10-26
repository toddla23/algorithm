t = int(input())
arr= list(map(int, input().split()))

answerArr = [i for i in arr]

for i in range(1, t):
  if(arr[i] < arr[i] + answerArr[i-1]):
    answerArr[i] = arr[i] + answerArr[i-1]
  # print(answerArr)
print(max(answerArr))