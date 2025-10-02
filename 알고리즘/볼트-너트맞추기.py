import sys

input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)


# 볼트와 너트의 비교: bolts[i] vs nuts[j]
# 반환값:
# (1) -1 if bolts[i] < nuts[j]
# (2) 0 if bolts[i] == nuts[j]
# (3) +1 if bolts[i] > nuts[j]


def cmp_bolt_nut(bolts, nuts, i, j):
    if bolts[i] < nuts[j]:
        return -1
    elif bolts[i] > nuts[j]:
        return +1
    else:
        return 0


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return


def calc(bolts, nuts, low, high, bolt_num, nut_num):
    if low >= high:
        return
    j = low
    target = low

    # 피벗이 볼트[low]임
    # 너트 정렬
    # print(f"pivot : {bolts[low]}")
    for i in range(low, high + 1):
        if cmp_bolt_nut(bolts=bolts, nuts=nuts, i=low, j=i) == 0:  # pivot == nut[i]
            target = i
        if cmp_bolt_nut(bolts=bolts, nuts=nuts, i=low, j=i) in [1, 0]:  # pivot > nut[i]

            # swap(nuts, i, j)
            nuts[i], nuts[j] = nuts[j], nuts[i]
            # swap(nut_num, i, j)
            nut_num[i], nut_num[j] = nut_num[j], nut_num[i]
            if bolts[low] == nuts[j]:
                target = j
            j += 1

    j -= 1

    # swap(nuts, target, j)
    nuts[target], nuts[j] = nuts[j], nuts[target]
    # swap(nut_num, target, j)
    nut_num[target], nut_num[j] = nut_num[j], nut_num[target]

    # print(f"nuts: {nuts}")
    # print(f"nuts_num: {nut_num}")
    k = low
    # 피벗이 볼트의 low 였던 nuts[j]임
    # 볼트 정렬

    for i in range(low, high + 1):
        if cmp_bolt_nut(bolts=bolts, nuts=nuts, i=i, j=j) == 0:  # pivot == nut[i]
            target = i
        if cmp_bolt_nut(bolts=bolts, nuts=nuts, i=i, j=j) in [-1, 0]:  # pivot > nut[i]
            # swap(bolts, i, k)
            bolts[i], bolts[k] = bolts[k], bolts[i]
            # swap(bolt_num, i, k)
            bolt_num[i], bolt_num[k] = bolt_num[k], bolt_num[i]
            if bolts[k] == nuts[j]:
                target = k
            k += 1
    k -= 1
    # print(f"target:{target}, k:{k}")
    # swap(bolts, target, k)
    bolts[target], bolts[k] = bolts[k],bolts[target]
    # swap(bolt_num, target, k)
    bolt_num[target], bolt_num[k] = bolt_num[k],bolt_num[target]
    # print(f"bolts: {bolts}")
    # print(f"bolt_num: {bolt_num}")
    # print(low, j, high)
    calc(
        bolts=bolts, nuts=nuts, low=low, high=j - 1, bolt_num=bolt_num, nut_num=nut_num
    )
    calc(
        bolts=bolts, nuts=nuts, low=j + 1, high=high, bolt_num=bolt_num, nut_num=nut_num
    )

    return


t = int(input())

for _ in range(t):
    n = int(input())
    bolts = list(map(int, input().split()))
    bolt_num = [i for i in range(n)]
    nuts = list(map(int, input().split()))
    nut_num = [i for i in range(n)]

    qwe = [0 for _ in range(n)]
    calc(bolts, nuts, 0, n - 1, bolt_num, nut_num)

    answer = [0 for _ in range(n)]
    for i in range(n):
        answer[bolt_num[i]] = nut_num[i] + 1
    print(" ".join(map(str, answer)))
