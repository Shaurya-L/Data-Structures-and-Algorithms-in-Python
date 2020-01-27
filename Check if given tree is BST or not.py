import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)
def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)
def isBST(root):
    if root == None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data <= leftMax:
        return False
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(isBST(root))
