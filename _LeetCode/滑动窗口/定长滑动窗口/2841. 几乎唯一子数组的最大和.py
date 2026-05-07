# -*- coding: utf-8 -*-
""" 中等
2841. 几乎唯一子数组的最大和

给你一个整数数组 nums 和两个正整数 m 和 k 。
请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
子数组指的是一个数组中一段连续 非空 的元素序列。

示例 1：
输入：nums = [2,6,7,3,1,7], m = 3, k = 4
输出：18
解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。
这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。

示例 2：
输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
输出：23
解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。

示例 3：
输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
输出：0
解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。

提示：
1 <= nums.length <= 2 * 10^4
1 <= m <= k <= nums.length
1 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        s_sum = sum(nums[:k])  # 初始和
        # 判断有 几乎唯一子数组： len(set(nums[:k])) >= m
        res = s_sum if len(set(nums[:k])) >= m else 0  # 默认有“几乎唯一子数组”

        for i in range(1, n - k + 1):
            s_sum += - nums[i - 1] + nums[i + k - 1]
            if len(set(nums[i: i + k])) >= m:
                res = max(res, s_sum)

        print(res)
        return res


if __name__ == '__main__':
    obj = Solution()
    obj.maxSum(nums=[2, 6, 7, 3, 1, 7], m=3, k=4)  # 18
    obj.maxSum(nums=[5, 9, 9, 2, 4, 5, 4], m=1, k=3)  # 23
    obj.maxSum(nums=[1, 2, 1, 2, 1, 2, 1], m=3, k=3)  # 0
    obj.maxSum(nums=[1, 1, 1, 3], m=2, k=2)  # 4
    obj.maxSum(nums=[2, 1, 1, 4], m=2, k=2)  # 5
