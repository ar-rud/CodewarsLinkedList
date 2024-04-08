"""
move node
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

def move_node(source, dest):
    """move"""
    dst = Node(source.data)
    dst.next = dest
    return Context(source.next, dst)
