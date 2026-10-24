""" 中等
82. 删除排序链表中的重复元素 II
给定一个 已排序 的链表的头节点 head。
删除原始链表中所有 重复 数字的节点，只留下 不同 的数字。
返回 已排序 的链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

提示：
    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按升序 排列
"""
from common.LinkList import *


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        cur = dummy = ListNode(next=head)  # 头节点前面添加一个哨兵节点（假节点）

        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:  # 后两个节点值相同
                # 值等于 val 的节点全部删除
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:  # 后两个节点值不同，就向后移动 1 位
                cur = cur.next
        print(linklist_to_list(dummy.next))
        return dummy.next


if __name__ == '__main__':
    obj = Solution()
    obj.deleteDuplicates(list_to_linklist([1, 2, 3, 3, 4, 4, 5]))
    obj.deleteDuplicates(list_to_linklist([1, 1, 1, 2, 3]))
    obj.deleteDuplicates(list_to_linklist([0, 0, 0, 0, 0]))
