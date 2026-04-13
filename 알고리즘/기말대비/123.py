import sys

sys.setrecursionlimit(10**7)


def pre_to_post(pre, l, r):
    if l > r:
        return []
    root = pre[l]
    m = l + 1
    while m <= r and pre[m] < root:
        m += 1
    left = pre_to_post(pre, l + 1, m - 1)
    right = pre_to_post(pre, m, r)
    # print(f"start: {l}, end: {r}, root: {root}")
    return left + right+ [root]


def post_to_pre(post, l, r):
    if l > r:
        return []
    root = post[r]
    m = r - 1
    while m >= l and post[m] > root:
        m -= 1
    left = post_to_pre(post, l, m)
    right = post_to_pre(post, m + 1, r - 1)
    return [root] + left + right


t = int(input())
for _ in range(t):
    dic = {}
    n, q = list(map(int, input().split()))
    temp = list(map(int, input().split()))

    inorder = temp[:]
    inorder.sort()
    if q == 1:
        root = pre_to_post(temp, 0, n - 1)

    if q == 2:
        root = post_to_pre(temp, 0, n - 1)
    print(" ".join(list(map(str,root))))