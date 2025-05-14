def change(color:str) -> str:
  if(color == 'W'):
    return "B"
  return 'W'

def check(arr:list):
  result1 = 0
  
  target_color = 'W'
  for col in range(8):
    target_color = change(target_color)
    for row in range(8):
      if(arr[col][row] == target_color):
        target_color = change(target_color)
      else:
        result1 += 1
        target_color = change(target_color)
        
  result2 = 0

  target_color = 'B'
  for col in range(8):
    target_color = change(target_color)
    for row in range(8):
      if(arr[col][row] == target_color):
        target_color = change(target_color)
      else:
        result2 += 1
        target_color = change(target_color)
        
  # print(result1, result2)
  return min(result1, result2)




col, row = map(int, input().split(" "))
arr = []
for i in range(col):
  arr.append(input())
  

answers = []
for i in range(0, col-8+1):
  for j in range(0,row-8+1):
    answers.append(check([arr[k][j:j+8] for k in range(i,i+8)]))
    
# print(answers)
print(min(answers))
