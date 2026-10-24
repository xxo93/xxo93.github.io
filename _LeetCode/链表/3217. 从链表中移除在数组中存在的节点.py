"""中等
3217. 从链表中移除在数组中存在的节点

给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。

示例 1：
输入： nums = [1,2,3], head = [1,2,3,4,5]
输出： [4,5]
解释：
移除数值为 1, 2 和 3 的节点。

示例 2：
输入： nums = [1], head = [1,2,1,2,1,2]
输出： [2,2,2]
解释：
移除数值为 1 的节点。

示例 3：
输入： nums = [5], head = [1,2,3,4]
输出： [1,2,3,4]
解释：
链表中不存在值为 5 的节点。
"""
from typing import Optional, List

from common.LinkList import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)  # 使用集合不超时
        pre = ListNode()
        pre.next = head
        curr = pre
        while curr.next:
            if curr.next.val in nums_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        print(linklist_to_list(pre.next))
        return pre.next


    def modifiedList_2(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """ 超时 """
        pre = ListNode()
        pre.next = head
        curr = pre
        while curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        print(linklist_to_list(pre.next))
        return pre.next


if __name__ == '__main__':
    obj = Solution()
    obj.modifiedList([1, 2, 3], list_to_linklist([1, 2, 3, 4, 5]))
    obj.modifiedList([1], list_to_linklist([1, 2, 1, 2, 1, 2]))
    obj.modifiedList([5], list_to_linklist([1, 2, 3, 4]))
