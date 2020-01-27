import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printAtK(root,k,lst):
    t=k
    if root is None:
        return
    if k==0 or t==0:
        print(root.data)
        return 0
    else:
        printAtK(root.left,k-1,lst)
        printAtK(root.right, t -1, lst)
def printkDistanceNodeDown(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
        return
    printkDistanceNodeDown(root.left,k-1)
    printkDistanceNodeDown(root.right,k-1)

def printkDistanceNode(root, target, k):
    if root is None: 
        return -1
    if root.data == target:
        printkDistanceNodeDown(root, k) 
        return 0 
    dl = printkDistanceNode(root.left, target, k) 
    if dl != -1: 
        if dl + 1 == k : 
            print(root.data)
        else: 
            printkDistanceNodeDown(root.right, k-dl-2) 
        return 1 + dl 
    dr = printkDistanceNode(root.right, target, k) 
    if dr != -1: 
        if (dr+1 == k): 
            print(root.data)
        else: 
            printkDistanceNodeDown(root.left, k-dr-2) 
        return 1 + dr 
    return -1

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
node = int(input())
k=int(input())
printkDistanceNode(root, node, k)
