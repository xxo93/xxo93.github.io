""" 简单
83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按升序 排列
"""
from common.LinkList import *


class Solution:

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """ 最优解法 """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def deleteDuplicates_2(self, head: ListNode | None) -> ListNode | None:
        pre = ListNode()
        pre.next = head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        print(linklist_to_list(pre.next))
        return pre.next


if __name__ == '__main__':
    obj = Solution()
    obj.deleteDuplicates(list_to_linklist([1, 1, 2]))
    obj.deleteDuplicates(list_to_linklist([1, 1, 2, 3, 3]))
    obj.deleteDuplicates(list_to_linklist([0, 0, 0, 0, 0]))
