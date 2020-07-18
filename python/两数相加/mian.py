class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    add = 0
    head = tmp = ListNode(None)
    # add　考虑最后一位进位的情况
    while(l1 is not None or l2 is not None or add):
        if l1 is None:
            one = 0
        else:
            one = l1.val

        if l2 is None:
            two = 0
        else:
            two = l2.val

        add = add + one + two;
        
        tmp.next = ListNode(add % 10)
        tmp = tmp.next
        add = add // 10

        # 链表长度不等的情况
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return head.next
