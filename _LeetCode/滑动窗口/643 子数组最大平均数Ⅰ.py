# -*- coding: utf-8 -*-
""" 简单
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10^-5 的答案都将被视为正确答案。

示例 1：
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

示例 2：
输入：nums = [5], k = 1
输出：5.00000

提示：
n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])  # 初始最大值

        s_max = res
        l1, l2 = 0, k - 1
        while l2 < len(nums) - 1:
            l1 += 1
            l2 += 1
            res = res - nums[l1 - 1] + nums[l2]
            s_max = max(s_max, res)

        return s_max / k


if __name__ == '__main__':
    obj = Solution()
    # print(obj.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))  # 12.75
    # print(obj.findMaxAverage(nums=[5], k=1))  # 5.00000
    # print(obj.findMaxAverage(nums=[0, 4, 0, 3, 2], k=1))  # 4
    print(obj.findMaxAverage(nums=[4, 2, 1, 3, 3], k=2))  # 2
