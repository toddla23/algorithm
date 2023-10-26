t = int(input())

arr = list(map(int, input().split(" ")))
answerArr = [1 for i in range(t)]

for i in range(t, -1 ,-1):
  for j in range(i, t):
    
    if(arr[j] < arr[i] and answerArr[j] >= answerArr[i]):
      # print('i:', i , 'j: ',j )
      answerArr[i] = answerArr[j] + 1
  # print(answerArr)
print(max(answerArr))
