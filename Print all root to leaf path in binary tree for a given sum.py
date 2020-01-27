import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printPathsUtil(root, sum, sum_so_far, path):
    if not root:
        return
    sum_so_far += root.data 
    path.append(root.data)  
    if (sum_so_far == sum ): 
        print(*path)  
    if (root.left != None): 
        printPathsUtil(root.left, sum, sum_so_far, path)  
    if (root.right != None):
        printPathsUtil(root.right, sum, sum_so_far, path) 
    path.pop(-1)  

def printPaths(root, sum): 
    path = [] 
    printPathsUtil(root, sum, 0, path)
    
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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
printPaths(root, k)

