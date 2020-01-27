import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder)==0:
        return None
    rootdata=postorder[-1]
    root=BinaryTreeNode(rootdata)
    count=0
    for i in range(len(inorder)-1):
        if inorder[i]==rootdata:
            break
        count+=1
    leftinorder=inorder[:count]
    rightinorder=inorder[count+1:]
    count1=len(leftinorder)
    leftpostorder=postorder[0:count1]
    rightpostorder=postorder[count1:len(postorder)-1]
    
    root.left=buildTreePostOrder(leftpostorder, leftinorder)
    root.right=buildTreePostOrder(rightpostorder, rightinorder)
    
    return root
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
