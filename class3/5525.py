n = int(input())
m = int(input())
s = input()

answer, i, count = 0, 0, 0

while i < (m - 1):
    if s[i : i + 3] == "IOI":
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
