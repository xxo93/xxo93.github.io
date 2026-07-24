# -*- coding: utf-8 -*-
""" 中等，固定滑动窗口(双端队列) + 哈希计数 + 贪心
3679. 使库存平衡的最少丢弃次数
给你两个整数 w 和 m，以及一个整数数组 arrivals，其中 arrivals[i] 表示第 i 天到达的物品类型（天数从 1 开始编号）。

物品的管理遵循以下规则：

- 每个到达的物品可以被 保留 或 丢弃 ，物品只能在到达当天被丢弃。
- 对于每一天 i，考虑天数范围为 [max(1, i - w + 1), i]（也就是直到第 i 天为止最近的 w 天）：
  - 对于 任何 这样的时间窗口，在被保留的到达物品中，每种类型最多只能出现 m 次。
  - 如果在第 i 天保留该到达物品会导致其类型在该窗口中出现次数 超过 m 次，那么该物品必须被丢弃。

返回为满足每个 w 天的窗口中每种类型最多出现 m 次，最少 需要丢弃的物品数量。

示例 1：
输入： arrivals = [1,2,1,3,1], w = 4, m = 2
输出： 0
解释：
第 1 天，物品 1 到达；窗口中该类型不超过 m 次，因此保留。
第 2 天，物品 2 到达；第 1 到第 2 天的窗口是可以接受的。
第 3 天，物品 1 到达，窗口 [1, 2, 1] 中物品 1 出现两次，符合限制。
第 4 天，物品 3 到达，窗口 [1, 2, 1, 3] 中物品 1 出现两次，仍符合。
第 5 天，物品 1 到达，窗口 [2, 1, 3, 1] 中物品 1 出现两次，依然有效。
没有任何物品被丢弃，因此返回 0。

示例 2：
输入： arrivals = [1,2,3,3,3,4], w = 3, m = 2
输出： 1
解释：
第 1 天，物品 1 到达。我们保留它。
第 2 天，物品 2 到达，窗口 [1, 2] 是可以的。
第 3 天，物品 3 到达，窗口 [1, 2, 3] 中物品 3 出现一次。
第 4 天，物品 3 到达，窗口 [2, 3, 3] 中物品 3 出现两次，允许。
第 5 天，物品 3 到达，窗口 [3, 3, 3] 中物品 3 出现三次，超过限制，因此该物品必须被丢弃。
第 6 天，物品 4 到达，窗口 [3, 4] 是可以的。
第 5 天的物品 3 被丢弃，这是最少必须丢弃的数量，因此返回 1。

提示：

1 <= arrivals.length <= 105
1 <= arrivals[i] <= 105
1 <= w <= arrivals.length
1 <= m <= w
"""
from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        q = deque()  # 窗口队列:存储 (位置, 类型) 的队列
        freq = defaultdict(int)  # 窗口元素频次
        discards = 0  # 丢弃的次数

        for i in range(len(arrivals)):
            # 1. 滑出窗口：移除超出范围的元素
            while q and q[0][0] < i - w + 1:
                _, val = q.popleft()
                freq[val] -= 1

            # 2. 检查当前类型在窗口中是否已达上限
            v = arrivals[i]
            if freq[v] >= m:
                discards += 1  # 超限，丢弃
            else:
                q.append((i, v))  # 保留，入队
                freq[v] += 1

        return discards


if __name__ == '__main__':
    obj = Solution()

    # obj.minArrivalsToDiscard(arrivals=[1, 2, 1, 3, 1], w=4, m=2)  # 0
    # obj.minArrivalsToDiscard(arrivals=[1, 2, 3, 3, 3, 4], w=3, m=2)  # 1
    # obj.minArrivalsToDiscard(arrivals=[1, 2, 3, 3, 3, 3, 3, 4], w=4, m=2)  # 2
    obj.minArrivalsToDiscard(arrivals=[1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 4], w=4, m=2)  # 4
