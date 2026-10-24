"""简单
203. 移除链表元素

premium lock icon相关企业
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]

提示：
    列表中的节点数目在范围 [0, 104] 内
    1 <= Node.val <= 50
    0 <= val <= 50
"""
from common.LinkList import ListNode, list_to_linklist, linklist_to_list


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        pre = ListNode()
        pre.next = head
        curr = pre
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        print(linklist_to_list(pre.next))
        return pre.next


if __name__ == '__main__':
    obj = Solution()
    obj.removeElements(list_to_linklist([1, 2, 6, 3, 4, 5, 6]), val=6)
    obj.removeElements(list_to_linklist([]), val=1)
    obj.removeElements(list_to_linklist([7, 7, 7, 7]), val=7)
