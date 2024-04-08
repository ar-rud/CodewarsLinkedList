"""linked_list_from_string"""
class Node:
    """node class"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """linked list from string"""
    return Node(data = int(s[:s.find(sepr)]), next = \
    linked_list_from_string(s[s.find(sepr)+4:])) if (sepr:= " -> ") in s else None
