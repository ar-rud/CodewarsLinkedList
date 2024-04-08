"""
remove duplicates
"""


class Node:
    """node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def remove_duplicates(head):
    prev = None
    cur = head
    while cur and cur.next:
        prev = cur
        cur = cur.next
        if prev.data == cur.data:
            while cur and cur.data == prev.data:
                cur = cur.next
            prev.next = cur
    return head
