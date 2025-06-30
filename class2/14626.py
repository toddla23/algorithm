s = list(input())

total = 0
starIdx = 0
for i in range(13):
    if s[i] == "*":
        starIdx = i
        continue
    else:
        total += int(s[i]) * 1 if i % 2 == 0 else int(s[i]) * 3
        # print(total)

for i in range(10):
    answer = (total +( i * 1 if starIdx % 2 == 0 else i*3)) % 10
    # print(answer)
    if answer == 0:
        print(i)
        break
