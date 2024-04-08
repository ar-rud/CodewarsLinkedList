"""
reverse
"""

class Node:
    """node class"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(head):
    """reverse"""
    if not head or not head.next:
        return head
    cur = head
    prev = None
    while cur.next:
        prev= cur
        cur = cur.next
    prev.next = None
    return Node(cur.data, reverse(head))
