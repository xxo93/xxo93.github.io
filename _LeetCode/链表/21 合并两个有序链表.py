# -*- coding: utf-8 -*-
"""
@auth: 30017121
@date: 2023/2/6 12:09
@desc: 简单
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例2：
输入：l1 = [], l2 = []
输出：[]

示例3：
输入：l1 = [], l2 = [0]
输出：[0]
"""
from typing import Optional

from python.LeetCode.common.LinkList import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        # 设定一个哨兵节点
        pre_head = ListNode(-1)
        pre_node = pre_head
        while p1 and p2:
            if p1.val <= p2.val:
                pre_node.next = p1
                p1 = p1.next
            else:
                pre_node.next = p2
                p2 = p2.next
            pre_node = pre_node.next

        # 合并后 l1 和 l2 最多只有1个还未被合并完，我们直接将链表末尾指向未合并完的链表即可（指向最后一个节点）
        pre_node.next = p1 if p1 is not None else p2

        return pre_head.next


if __name__ == '__main__':
    obj = Solution()

    l1 = list_to_linklist([1, 2, 4])
    l2 = list_to_linklist([1, 3, 4])
    print(linklist_to_list(obj.mergeTwoLists(l1, l2)))

    l1 = list_to_linklist([])
    l2 = list_to_linklist([])
    print(linklist_to_list(obj.mergeTwoLists(l1, l2)))

    l1 = list_to_linklist([1])
    l2 = list_to_linklist([])
    print(linklist_to_list(obj.mergeTwoLists(l1, l2)))
