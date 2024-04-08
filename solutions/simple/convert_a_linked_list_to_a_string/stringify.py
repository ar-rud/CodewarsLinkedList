"""
stringify
"""

class Node:
    """node class"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def stringify(node):
    """stringify"""
    cur = node
    res = ""
    while cur:
        res += str(cur.data)
        res += " -> "
        cur = cur.next
    return res + str(cur)
