s = list(input())
targetStr = list(input())

lastWord = targetStr[-1]
stack = []
for i in range(len(s)):
    word = s[i]
    stack.append(word)
    if word == lastWord:
        isTarget = True
        for j in range(len(targetStr)-1,-1, -1):
            # print(stack)
            # print(f"{len(stack)} - {len(targetStr)} + {j}")
            if stack[len(stack) - len(targetStr) + j] != targetStr[j]:
                isTarget = False
                break
        
        if isTarget:
            for j in range(len(targetStr)):
                stack.pop()

# print(stack)
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
