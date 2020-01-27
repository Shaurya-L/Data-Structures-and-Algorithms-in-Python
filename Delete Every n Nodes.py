class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if M==0:
        return None
    if N==0:
        return head
    t1 = head
    while t1 is not None:
        c1 = 1
        while(c1 < M):
            if t1 is not None:
                t1 = t1.next
                c1 += 1
            else:
                return head
        t2 = t1.next
        c2 = 1
        while(c2 < N):
            if t2 is not None:
                t2 = t2.next
                c2 += 1   
            else:
                t1.next = t2
                return head

        if t2 is not None:    
            t2 = t2.next
            t1.next = t2
            t1 = t2
        else:
            t1.next = t2
            return head
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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l) 
