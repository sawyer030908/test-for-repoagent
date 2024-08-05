class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    cur1 = l1
    cur2 = l2
    if cur1.val + cur2.val > 9:
        result = ListNode(cur1.val + cur2.val - 10)
        p = 1
    else:
        result = ListNode(cur1.val + cur2.val)
        p = 0
    ans = result
    cur1 = cur1.next
    cur2 = cur2.next
    while cur1 is not None and cur2 is not None:
        item = p
        item += cur1.val + cur2.val
        if item > 9:
            p = 1
            item -= 10
        else:
            p = 0
        result.next = ListNode(item)
        result = result.next
        cur1 = cur1.next
        cur2 = cur2.next
    if cur1 is None:
        cur = cur2
    else:
        cur = cur1
    while cur is not None:
        item = p + cur.val
        if item > 9:
            p = 1
            item -= 10
        else:
            p = 0
        result.next = ListNode(item)
        result = result.next
        cur = cur.next
    if p == 1:
        result.next = ListNode(1)
    return ans