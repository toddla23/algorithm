import sys


def calc(n: int) -> int:
    answer = 0

    k = 1
    empty = 0
    while k <= n:
        temp = n - empty
        empty += k
        k = k * 2
        answer += temp
        # print(f"k: {k}, empty: {empty}, count: {temp}, answer:{answer}")
    # print(answer)
    return answer


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(calc(n))
