class Node:
    def __init__(self, next=None):
        self.next = next
        
def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    curr = head
    while curr and curr.next:
        next_pair = curr.next.next
        second = curr.next
        second.next = curr
        curr.next = next_pair
        if prev:
            prev.next = second
        prev = curr
        curr = next_pair
    return new_head
