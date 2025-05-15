n = int(input())
arr= []

for _ in range(n):
  arr.append(int(input()))
arr.reverse()

answer = [1]
target = 0
answer_row = ["+"]
count = 1

while count <= max(arr):
  print('________________________________________')
  print(f"count: {count+1}" )
  
  if(len(answer)!=0 and arr[-1] == answer[-1]):
    answer.pop()
    answer_row.append("-")
    arr.pop()
    print(f"arr: {arr}")
    print(f"answer: {answer}")
    print(f"answer_row: {answer_row}")

  else:
    count += 1
    answer.append(count)
    answer_row.append("+")
    # print(f"arr: {arr}")
    # print(f"answer: {answer}")
    # print(f"answer_row: {answer_row}")


for i in range(len(arr)):
  if(arr[i] == answer[i]):
    answer_row.append('-')
  else:
    answer_row = 'NO'
    break
  
if(answer_row == 'NO'):
  print('NO')  
else:
  for i in answer_row:
    print(i)