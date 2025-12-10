import sys

sys.setrecursionlimit(10**7)


def postToTree(postOrder, inOrder):
    # print(postOrder, inOrder)
    global dic
    if len(postOrder) <= 0:
        return 0
    if len(postOrder) == 1:
        dic[postOrder[0]] = [0, 0]
        return postOrder[0]

    root = postOrder[-1]
    rootSpot = inOrder.index(root)
    postOrderLeft = postOrder[0:rootSpot]
    postOrderRight = postOrder[rootSpot : len(postOrder) - 1]
    inOrderLeft = inOrder[0:rootSpot]
    inOrderRight = inOrder[rootSpot + 1 :]

    leftRoot = postToTree(postOrderLeft, inOrderLeft)
    rightRoot = postToTree(postOrderRight, inOrderRight)

    # print(f"root: {root}, left: {leftRoot}, right: {rightRoot}")

    dic[root] = [leftRoot, rightRoot]

    return root


def preToTree(preOrder, inOrder):
    global dic
    if len(preOrder) == 0:
        return 0
    if len(preOrder) == 1:
        dic[preOrder[0]] = [0, 0]
        return preOrder[0]
    
    root = preOrder[0]
    rootSpot = inOrder.index(root)
    preOrderLeft = preOrder[1 : rootSpot + 1]
    preOrderRight = preOrder[rootSpot + 1 :]
    inOrderLeft = inOrder[0:rootSpot]
    inOrderRight = inOrder[rootSpot + 1 :]

    leftRoot = preToTree(preOrderLeft, inOrderLeft)
    rightRoot = preToTree(preOrderRight, inOrderRight)

    dic[root] = [leftRoot, rightRoot]
    return root


def preOrder(dic, root, answer):
    answer.append(root)
    if dic[root][0] != 0:
        preOrder(dic, dic[root][0], answer)

    if dic[root][1] != 0:
        preOrder(dic, dic[root][1], answer)
    return


def postOrder(dic, root, answer):
    if dic[root][0] != 0:
        postOrder(dic, dic[root][0], answer)
    if dic[root][1] != 0:
        postOrder(dic, dic[root][1], answer)
    answer.append(root)

    return


t = int(input())
for _ in range(t):
    dic = {}
    n, q = list(map(int, input().split()))
    temp = list(map(int, input().split()))

    inorder = temp[:]
    inorder.sort()
    if q == 1:
        root = preToTree(temp, inorder)
        # print(dic),
        answer = []
        postOrder(dic, root, answer)
        print(" ".join(list(map(str, answer))))

    if q == 2:
        root = postToTree(temp, inorder)
        # print(dic)
        answer = []
        preOrder(dic, root, answer)
        print(" ".join(list(map(str, answer))))


