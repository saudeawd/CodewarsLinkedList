class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    if head is None or head.data > data:
        n = Node(data)
        n.next = head
        return n
    head.next = sorted_insert(head.next, data)
    return head
