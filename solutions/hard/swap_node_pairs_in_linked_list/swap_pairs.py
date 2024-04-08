"""
swap node pairs
"""

class Node:
    """node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    prev = None
    cur = head
    while cur and cur.next:
        second = cur.next
        if prev:
            prev.next = second
        else:
            head = second
        cur.next = second.next
        second.next = cur
        
        prev = cur
        cur = cur.next
    return head
