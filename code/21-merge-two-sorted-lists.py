from linked_list import list_node_to_iter, list_node_from_iter
from iterator import merge

def mergeTwoLists(l1,l2):
    return list_node_from_iter(merge(min, map(list_node_to_iter, [l1,l2])))
