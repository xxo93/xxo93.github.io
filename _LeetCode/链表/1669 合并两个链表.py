# -*- coding: utf-8 -*-
""" 中等
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。

请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。
"""
from python.LeetCode.common.LinkList import list_to_linklist, ListNode, linklist_to_list


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        sub1_end = list1
        p1 = a - 1
        while p1:
            sub1_end = sub1_end.next
            p1 -= 1

        # 去除的链表的左侧节点
        remove_left_node = sub1_end.next
        # 指向链表2
        sub1_end.next = list2

        # 找到第1个链表的右链表的头节点
        remove_right_node = remove_left_node
        p2 = b - a
        while p2 > 0:
            remove_right_node = remove_right_node.next
            p2 -= 1
        sub2_head = remove_right_node.next

        # 遍历第二个链表的最后一个节点
        p_node = list2
        while p_node.next is not None:
            p_node = p_node.next

        # 将第2个链表的尾节点指向第1个链表的右链表的头节点
        p_node.next = sub2_head

        return list1


if __name__ == '__main__':
    obj = Solution()

    res_head = obj.mergeInBetween(
        list_to_linklist([0, 1, 2, 3, 4, 5]),
        3, 4,
        list_to_linklist([1000000, 1000001, 1000002])
    )
    print(linklist_to_list(res_head))

    res_head = obj.mergeInBetween(
        list_to_linklist([0, 1, 2, 3, 4, 5, 6]),
        2, 5,
        list_to_linklist([1000000, 1000001, 1000002, 1000003, 1000004])
    )
    print(linklist_to_list(res_head))
