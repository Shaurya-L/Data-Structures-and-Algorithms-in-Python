import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def constructBST(lst):
    if not lst:
        return None
    mid = (len(lst) - 1)//2
    root = BinaryTreeNode(lst[mid])
    l = constructBST(lst[:mid])
    r = constructBST(lst[mid + 1:])
    root.left = l
    root.right = r
    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
lst.sort()
root=constructBST(lst)
preOrder(root)
