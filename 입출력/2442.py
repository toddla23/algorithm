t = int(input()) + 1
totalLength = t * 2 - 1

for i in range(1, t):
  starCount = i*2-1
  spaceCount = (totalLength - starCount) // 2 - 1
  # print("starCount:", starCount)
  # print("spaceCount:", spaceCount)
  print(" " * spaceCount + "*" * starCount )