# -*- coding: utf-8 -*-
""" 中等
最适合链表的排序算法是“归并排序”, 涉及链表排序 leetcode21

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例3：
输入：head = []
输出：[]
"""
from typing import Optional

from python.LeetCode.common.LinkList import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def sortList_bubbling(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 冒泡: 超时
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        # 空节点或单节点链表
        if not head or (head.val is None or head.val == 0) or (head.next is None):
            return head
        p = head
        tail = None
        while tail != head:
            while p.next != tail:
                if p.val > p.next.val:
                    p.val, p.next.val = p.next.val, p.val
                p = p.next
            tail = p
            p = head
        return head

    def sortList_merge(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 归并排序，涉及链表排序 leetcode21
        时间复杂度：O(n log n)
        空间复杂度：
        """

        return head


if __name__ == '__main__':
    obj = Solution()

    # 冒泡排序
    # head = list_to_linklist([4, 2, 1, 3])
    # print(linklist_to_list(obj.sortList_bubbling(head)) == [1, 2, 3, 4])
    #
    # head = list_to_linklist([-1, 5, 3, 4, 0])
    # print(linklist_to_list(obj.sortList_bubbling(head)) == [-1, 0, 3, 4, 5])
    #
    # head = list_to_linklist([])
    # print(linklist_to_list(obj.sortList_bubbling(head)))

    # 归并排序
    head = list_to_linklist([4, 2, 1, 3])
    print(linklist_to_list(obj.sortList_merge(head)) == [1, 2, 3, 4])

    head = list_to_linklist([-1, 5, 3, 4, 0])
    print(linklist_to_list(obj.sortList_merge(head)) == [-1, 0, 3, 4, 5])

    head = list_to_linklist([])
    print(linklist_to_list(obj.sortList_merge(head)))
