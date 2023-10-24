t = int(input())
arr= list(map(int, input().split(" ")))
answerArr = [1 for i in range (t)]

for i in range(t):
  temp = 0
  for j in range(i):
    if(arr[i] > arr[j] and answerArr[i] <= answerArr[j]):
      answerArr[i] = answerArr[j] + 1
    # print('arr[i]' , arr[i],'arr[j]', arr[j])
    # print(answerArr)
    


print(max(answerArr))