def findMergeNode(head1, head2):
    orig = head1
    while True:
        head1 = orig
        while head1 is not None:
            if head1 == head2:
                return head1.data
            head1 = head1.next
        head2 = head2.next
