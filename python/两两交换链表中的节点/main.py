class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head

    l1 = head.next
    head.next = swapPairs(head.next.next)
    l1.next = head

    return l1
