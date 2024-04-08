"""
alternating split
"""

class Node:
    """node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Context(object):
    """context class"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def alternating_split(head):
    assert head and head.next
    res = Context((cur1 := Node(head.data)), (cur2 := Node(head.next.data)))
    counter = 1
    cur = Node()
    cur.next = head.next.next
    while not cur or cur.next:
        cur = cur.next
        if counter & 1:
            cur1.next = cur
            cur1 = cur1.next if cur1 else cur1
        else:
            cur2.next = cur
            cur2 = cur2.next if cur2 else cur2
        counter += 1
    cur1.next = None
    cur2.next = None        
    return res
