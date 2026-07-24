# -*- coding: utf-8 -*-
"""
简单 中等 链表
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
                             ↓---------¬
输入：head = [3,2,0,-4]  3 -> 2 -> 0 -> -4 , pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 判断链表是否有环：单指针遍历  """
        if not head:
            return False
        visited = set()
        p = head
        while p.next:
            visited.add(p)
            p = p.next
            if p in visited:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """ 判断链表是否有环：快慢指针 """
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next
            slow = slow.next
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 单指针判断是否访问 """
        if not head:
            return None
        visited = set()
        p = head
        while p.next:
            visited.add(p)
            p = p.next
            if p in visited:
                return p
        return None


if __name__ == '__main__':
    obj = Solution()

    a = ListNode(1)
    b = ListNode(2)

    a.next = b
    b.next = a

    obj.detectCycle(a)
