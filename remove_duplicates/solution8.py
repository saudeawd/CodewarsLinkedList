class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    node = head
    while node:
        if node.next and node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head
