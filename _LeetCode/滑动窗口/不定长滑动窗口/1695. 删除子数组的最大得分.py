""" 中等
1695. 删除子数组的最大得分

给你一个正整数数组 nums ，请你从中删除一个含有 【若干[不同]元素】 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]

示例 2：
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]

提示：
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
"""
from collections import defaultdict
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """ 更优解 """
        ans = left = 0
        cnt = defaultdict(int)
        max_ans = 0
        for right, n in enumerate(nums):
            cnt[n] += 1

            while cnt[n] > 1:
                cnt[nums[left]] -= 1
                ans -= nums[left]
                left += 1

            ans += n
            max_ans = max(ans, max_ans)

        print(max_ans)
        return max_ans

    def maximumUniqueSubarray_2(self, nums: List[int]) -> int:
        """ 次优解 """
        ans = left = 0
        cnt = defaultdict(int)

        for right, n in enumerate(nums):
            cnt[n] += 1

            while cnt[n] > 1:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, sum(nums[left:right + 1]))
        print(ans)
        return ans


if __name__ == '__main__':
    obj = Solution()
    obj.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6])  # 17
    obj.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5])  # 8
    obj.maximumUniqueSubarray(nums=[10000, 1, 10000, 1, 1, 1, 1, 1, 1])  # 10001
