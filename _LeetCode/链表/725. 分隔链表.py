""" 中等
725. 分隔链表
给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
返回一个由上述 k 部分组成的数组。

示例 1：
输入：head = [1,2,3], k = 5
输出：[[1],[2],[3],[],[]]
解释：
第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。

示例 2：
输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
输出：[[1,2,3,4],[5,6,7],[8,9,10]]
解释：
输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。

提示：
链表中节点的数目在范围 [0, 1000]
0 <= Node.val <= 1000
1 <= k <= 50
"""
from _LeetCode.common.LinkList import ListNode, list_to_linklist, linklist_to_list

class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        """
        1. 先是遍历链表的长度 n
        2. 计算分割后每段的较小长度 n // k，其中前 n%k 段比其他段长 1
        """
        n = 0  # 链表长度
        node = head
        while node:
            n += 1
            node = node.next

        avg_len = n // k  # 每段长度至少为 avg_len
        before_x = n % k  # 前 x 段, 前 x 段的长度 为 avg_len + 1

        parts = [None for _ in range(k)]
        i, curr = 0, head
        while i < k and curr:
            parts[i] = curr

            part_size = avg_len + (1 if i < before_x else 0)  # 每段长度，在 第 i 段之前的时候 需要 +1
            for _ in range(part_size - 1):
                curr = curr.next

            _next_head = curr.next  # 拿到下一段的头节点
            curr.next = None        # 上一段的尾节点指空
            curr = _next_head       # 当前节点重新指向下一段的头节点
            i += 1

        return parts


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)

    obj = Solution()
    obj.splitListToParts(head, 3)






