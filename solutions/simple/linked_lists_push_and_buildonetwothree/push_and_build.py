"""push_and_build"""

class Node:
    """node class"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def push(head, data):
    """push"""
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """build 1 2 3"""
    cur = None
    for i in range(3, 0, -1):
        temp = cur
        cur = Node(i)
        cur.next = temp
    return cur
