""" 中等
1052. 爱生气的书店老板
有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，
其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。
在某些分钟内，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。

示例 1：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

示例 2：
输入：customers = [1], grumpy = [0], minutes = 1
输出：1

提示：
    n == customers.length == grumpy.length
    1 <= minutes <= n <= 2 * 104
    0 <= customers[i] <= 1000
    grumpy[i] == 0 or 1

"""
from mimetypes import init


class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        1. 先统计 老板不生气的顾客数量（grumpy[i]为 0 时的总数）base
        2. 在通过滑动窗口 minutes 遍历滑动统计 grumpy[i]为 1 时的最大数量 maxAdd
        3. 结果 total = base + maxAdd

        [1, 0, 1, 2, 1, 1, 7, 5],
        [0, 1, 0, 1, 0, 1, 0, 1]
        """
        n = len(customers)
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        init_count = sum(c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1)
        max_count = init_count

        for i in range(n - minutes):
            if grumpy[i] == 1:
                init_count -= customers[i]
            if grumpy[i + minutes] == 1:
                init_count += customers[i + minutes]
            max_count = max(max_count, init_count)

        res = base + max_count
        print(res)
        return res


if __name__ == '__main__':
    obj = Solution()

    obj.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3)  # 16
    obj.maxSatisfied(customers=[1], grumpy=[0], minutes=1)  # 1
