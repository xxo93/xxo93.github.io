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

from common.LinkList import ListNode, list_to_linklist, linklist_to_list


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 快慢指针，完美解法 """
        slow = fast = head  # 乌龟和兔子同时从起点出发
        while fast and fast.next:
            slow = slow.next  # 乌龟走一步
            fast = fast.next.next  # 兔子走两步
            if fast is slow:  # 兔子追上乌龟（套圈），说明有环
                return True
        return False  # 访问到了链表末尾，无环

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 判断链表是否有环：快慢指针 """
        if not head or not head.next:
            return False

        p1 = p2 = head
        while p2 and p2.next:
            if p1 is p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False


if __name__ == '__main__':
    obj = Solution()

   # 1, 2, 3, 4, 5, 3
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a3

    # print(linklist_to_list(a1))


    print(obj.hasCycle(a1))
