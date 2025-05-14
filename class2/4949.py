while True:
  arr = input()
  if arr == '.':
    break
  
  brakets = []
  answer = 'yes'
  
  for i in arr:
    if(i in ['(', '[']):
      brakets.append(i)
    # print(brakets)
    if(i in [')', ']'] ):
      if brakets:
        temp = brakets.pop()
        if temp == "(" and i != ')':
          answer = 'no'
          break
        if temp == "[" and i != ']':
          answer = "no"
          break
      else:
        answer = 'no'
        break
  
  if(len(brakets)):
    answer = "no"
  print(answer)
      
        
  
  