import math

t = int(input())
answerArr = [i for i in range(t+1)]
for i in range (1, t+1):
  tempArr = []
  for j in range(1, int(math.sqrt(i)) + 1):
    idx = i - j**2
    tempArr.append(1 + answerArr[idx])
  # print(tempArr)
  # print('i: ', i , "tempArr: ", tempArr, 'answerArr: ', answerArr)
  answerArr[i] = (min(tempArr))
print(answerArr[t])