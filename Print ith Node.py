class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def ithNode(head, i):
    count = 0
    while head is not None:
        if count == i:
            return head.data
        count = count + 1
        head = head.next
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i=int(input())
node = ithNode(l, i)
if node is None:
    pass
else:
    print(node)
