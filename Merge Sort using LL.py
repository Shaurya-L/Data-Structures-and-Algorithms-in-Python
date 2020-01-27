class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def midpoint_linkedlist(head):
    slow = head
    fast = head
    while fast.next and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
def merge(head1,head2):
    final_head = None
    final_tail = None
    if head1.data < head2.data:
        final_head = head1
        final_tail = head1
        head1 = head1.next
        while head1 != None and head2 != None:
            if head1.data > head2.data:
                final_tail.next = head2
                final_tail = final_tail.next
                head2 = head2.next
            else:
                final_tail.next = head1
                final_tail = final_tail.next
                head1 = head1.next
    else:
        final_head = head2
        final_tail = head2
        head2 = head2.next
        while head1 != None and head2 != None:
            if head1.data > head2.data:
                final_tail.next = head2
                final_tail = final_tail.next
                head2 = head2.next
            else:
                final_tail.next = head1
                final_tail = final_tail.next
                head1 = head1.next
    if(head1 is not None):
        final_tail.next=head1
    if(head2 is not None):
        final_tail.next=head2
    return final_head
def length(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count
def mergeSort(head):
    if length(head) == 0 or length(head) == 1:
        return head
    mid = midpoint_linkedlist(head)
    head2 = mid.next
    mid.next = None
    left=mergeSort(head)
    right=mergeSort(head2)
    shead=merge(left,right)
    return shead
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
l = mergeSort(l)
printll(l)
