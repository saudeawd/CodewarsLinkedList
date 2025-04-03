def linked_list_from_string(s):
    lst = s.split(" -> ")[:-1]
    node = None
    while lst:
        node = Node(int(lst.pop()), node)
    return node