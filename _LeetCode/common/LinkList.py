# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linklist(node_list: list) -> [ListNode, None]:
    """ 给定列表，生成链表 """
    if len(node_list) == 0:
        # 空链表
        return None
    header = ListNode(node_list[0])
    p = header
    for node_val in node_list[1:]:
        nxt = ListNode(node_val)
        p.next = nxt
        p = p.next
    return header


def linklist_to_list(header: ListNode) -> list:
    """ 给定链表，生成列表 """
    node_val_list = []
    p = header
    while p:
        node_val_list.append(p.val)
        p = p.next
    return node_val_list
