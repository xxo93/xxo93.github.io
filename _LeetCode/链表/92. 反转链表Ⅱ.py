""" 中等
92. 反转链表 II

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5]

提示：
    链表中节点数目为 n
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
"""
from common.LinkList import *


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(next=head)
        # 遍历到 left 前一个节点位置
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        # 反转链表
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre  # 反转指针
            pre = cur  # pre 指针后移
            cur = nxt  # cur 指针后移

        p0.next.next = cur
        p0.next = pre
        return dummy.next


if __name__ == '__main__':
    obj = Solution()
    obj.reverseBetween(list_to_linklist([1, 2, 3, 4, 5]))
    obj.reverseBetween(list_to_linklist([5]))
