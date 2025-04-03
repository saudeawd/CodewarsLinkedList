class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    a = Node(data)
    a.next = head
    return a
  
def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
