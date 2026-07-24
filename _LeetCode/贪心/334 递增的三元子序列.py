# -*- coding: utf-8 -*-
""" 贪心 数组
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意

示例 2：
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组

示例 3：
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

提示：
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？

"""
from typing import List


class Solution:
    """
    1.维护两个变量：
    first：当前找到的最小候选值（可能是三元组的第一个数）。
    second：比 first 大的最小候选值（可能是三元组的第二个数）。

    2.遍历数组：
    如果当前元素 num 小于等于 first，更新 first = num（尝试找到更小的起点）。
    否则，如果 num 小于等于 second，更新 second = num（找到比 first 大的最小候选值）。
    如果 num 大于 second，说明找到了满足 first < second < num 的三元组，返回 true。

    3.终止条件：
    如果遍历完数组仍未找到满足条件的三元组，返回 false
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == '__main__':
    obj = Solution()

    # print(obj.increasingTriplet([5, 4, 3, 2, 1]))
    print(obj.increasingTriplet([2, 1, 5, 0, 4, 6]))
