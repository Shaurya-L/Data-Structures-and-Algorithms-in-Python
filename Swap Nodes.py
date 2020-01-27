class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def swap_nodes(head, i, j):
    p1 = None
    p2 = None
    c1 = None
    c2 = None
    temp = head
    prev = None
    cnt = 0
    while temp is not None:
        if(cnt == i):
            p1 = prev
            c1 = temp
        if (cnt == j):
            p2 = prev
            c2 = temp
            break
        prev = temp
        temp = temp.next
        cnt += 1
    if p1 is not None: 
        p1.next = c2
    p2.next = c1
    next = c1.next
    c1.next = c2.next
    c2.next = next
    
    if p1 is None:
        return c2
    else:
        return head
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
i, j=list(int(i) for i in input().strip().split(' '))
if i > j:
    l = swap_nodes(l, j, i)
else:
    l = swap_nodes(l, i, j)
printll(l)
