def loop_size(node):
    node_set = {}
    node_idx = 0
    while True:
        if node not in node_set:
            node_set[node] = node_idx
            node = node.next
            node_idx += 1
        else:
            loop_start = node_set[node]
            return node_idx - loop_start
