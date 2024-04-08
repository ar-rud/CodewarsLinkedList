"""
sorted insertion
"""

class Node:
    """node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    if not head:
        return Node(data)
    cur = head
    if data < head.data:
        res = Node(data)
        res.next = head
        return res
    while cur:
        if not cur.next:
            cur.next = Node(data)
            break
        if cur.data < data < cur.next.data:
            end = cur.next
            new_node = Node(data)
            new_node.next = end
            cur.next = new_node
            break
        cur = cur.next
    return head
