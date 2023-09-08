t = int(input())

totalLength = t*2 - 1

for i in range(t, 1, -1):
  starLength = i*2 - 1
  blankLength = (totalLength - starLength) // 2 
  print(" " * blankLength+ "*" * starLength)

for i in range(1, t+1):
  starLength = i*2 - 1
  blankLength = (totalLength - starLength) // 2 
  print(" " * blankLength+ "*" * starLength)