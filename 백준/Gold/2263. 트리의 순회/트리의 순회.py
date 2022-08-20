import sys; gets = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(gets())
inorder = list(map(int, gets().split()))
postorder = list(map(int, gets().split()))

nodeNum = [0] * (n+1)
for i in range(n):
    nodeNum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd]
    print(root, end=" ")

    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]

    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n-1, 0, n-1)

