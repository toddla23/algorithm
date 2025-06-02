for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        wear, case = input().split(" ")
        dic.setdefault(case, []).append(wear)

    answer = 1
    for key in dic.keys():
        answer = answer * (len(dic[key]) + 1)
    print(answer - 1)
