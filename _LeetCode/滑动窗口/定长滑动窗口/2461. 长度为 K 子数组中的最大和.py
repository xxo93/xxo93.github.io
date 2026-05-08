# -*- coding: utf-8 -*-
""" 中等
2461. 长度为 K 子数组中的最大和

给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：
- 子数组的长度是 k，且
- 子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。
子数组 是数组中一段连续非空的元素序列。

示例 1：
输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。

示例 2：
输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。

提示：
1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from typing import List
from collections import Counter, defaultdict


class Solution:
    def maximumSubarraySum_超时(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = sum(nums[:k])
        res = s
        if len(set(nums[:k])) < k:  # 使用set开销较大，耗时。（list转set的时候每个窗口都需要遍历每个元素）
            res = 0
        for i in range(1, n - k + 1):
            s += - nums[i - 1] + nums[i + k - 1]
            if len(set(nums[i:i + k])) == k:
                res = max(res, s)
        print(res)
        return res

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window_sum = sum(nums[:k])  # 初始的sum
        cnt = Counter(nums[:k])
        res = window_sum  # 符合条件：res=window_sum （即“初始的sum”）
        if len(cnt) < k:  # 不符合条件：res=0
            res = 0
        for i in range(1, n - k + 1):
            _out, _in = nums[i - 1], nums[i + k - 1]  # 出队元素:i-1； 入队元素:i+k-1
            window_sum += - _out + _in  # 计算每个窗口的sum变化
            # 统计入队出队的元素的频次
            cnt[_out] -= 1
            cnt[_in] += 1
            # 将频次为0的元素移除，再比较是否符合条件
            if cnt[nums[i - 1]] == 0:
                cnt.pop(_out)
            if len(cnt) == k:  # 符合条件
                res = max(res, window_sum)

        print(res)
        return res

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)

        left = 0
        window_sum = 0
        ans = 0

        for right, x in enumerate(nums):
            cnt[x] += 1
            window_sum += x

            # 保持窗口大小为 k
            if right - left + 1 > k:
                y = nums[left]
                cnt[y] -= 1

                if cnt[y] == 0:
                    del cnt[y]

                window_sum -= y
                left += 1

            # 判断是否满足 distinct
            if right - left + 1 == k and len(cnt) == k:
                ans = max(ans, window_sum)
        print(ans)
        return ans


if __name__ == '__main__':
    obj = Solution()
    obj.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3)  # 15
    obj.maximumSubarraySum(nums=[4, 4, 4], k=3)  # 0
    obj.maximumSubarraySum(nums=[4, 4, 4, 4, 4, 1, 2], k=3)  # 7
    obj.maximumSubarraySum(nums=[1, 3, 4, 4, 4, 4, 4], k=3)  # 8
