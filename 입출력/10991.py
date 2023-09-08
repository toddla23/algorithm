t = int(input()) # 2
totalLength = t * 2 -1 # 3

for i in range(1, t + 1):
  starLength= i * 2 - 1 #3
  blankLength = (totalLength - starLength) // 2 #0
  print(" " * blankLength, end="")
  for j in range(starLength): #3
    # print(j, end="")
    if j % 2 == 0:
      print("*", end="")
    else:
      print(" ", end="")
  print()