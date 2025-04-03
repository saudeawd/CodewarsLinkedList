class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("invalid parameters.")
    while index > 0:
        if node.next is None:
            raise Exception("Null node encountered.") 
        node = node.next
        index -= 1
    return node