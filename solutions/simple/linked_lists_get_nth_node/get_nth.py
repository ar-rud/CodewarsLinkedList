"""
get nth node
"""

class Node:
    """node class"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """get nth node"""
    if index < 0 or not node:
        raise ArgumentException
    cur = node
    for _ in range(index):
        try:
            cur = cur.next
        except AttributeError:
            raise ArgumentException
        if not cur:
            raise ArgumentException
    return cur.data if isinstance(cur, Node) else cur
