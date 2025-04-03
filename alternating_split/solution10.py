class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()

    first_head, second_head = head, head.next
    probe, next_probe = head, head.next

    while probe is not None and next_probe is not None:
        probe.next = next_probe.next
        probe = probe.next
        if probe:
            next_probe.next = probe.next
            next_probe = next_probe.next

    if probe:
        probe.next = None

    return Context(first_head, second_head)
