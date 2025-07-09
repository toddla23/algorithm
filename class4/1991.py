import sys

input = sys.stdin.readline


def preOrder(tree: dict, node: str):
    print(node,end="")
    if tree[node][0] != ".":
        preOrder(tree, tree[node][0])
    if tree[node][1] != ".":
        preOrder(tree, tree[node][1])
        
def inOrder(tree: dict, node: str):
    if tree[node][0] != ".":
        inOrder(tree, tree[node][0])
    print(node,end="")
    if tree[node][1] != ".":
        inOrder(tree, tree[node][1])
        
def postOrder(tree: dict, node: str):
    if tree[node][0] != ".":
        postOrder(tree, tree[node][0])
    if tree[node][1] != ".":
        postOrder(tree, tree[node][1])
    print(node,end="")


n = int(input())

tree = {}
for _ in range(n):
    a, b, c = input().rstrip().split(" ")
    tree[a] = (b, c)

preOrder(tree=tree, node="A")
print('')
inOrder(tree=tree, node="A")
print('')
postOrder(tree=tree, node="A")


