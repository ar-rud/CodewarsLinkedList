"""
loop size
"""

class Node:
    """node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    fast = node
    slow = node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            slow = node

            while slow != fast:
                slow = slow.next
                fast = fast.next

            leng = 1
            fast = fast.next
            while fast != slow:
                fast = fast.next
                leng += 1

            return leng
