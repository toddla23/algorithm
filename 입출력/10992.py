t = int(input())

totalLength = t * 2 - 1

print(" " * ((totalLength - 1) // 2)+ "*")
for i in range(2, t):
  starCount = i * 2 - 1
  blankLength = (totalLength - starCount) // 2
  middleBlankLength = starCount - 2
  print(" " * blankLength + "*" + " " * middleBlankLength + "*")

print("*" * totalLength)