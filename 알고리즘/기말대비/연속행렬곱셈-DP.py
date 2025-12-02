def matrix_chain_order(d):
    return

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    d = list(map(int, input().strip().split()))
    dp, split = matrix_chain_order(d)
    