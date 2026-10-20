""" 中等
1004. 最大连续1的个数 III

给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。

示例 1：
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。

提示：
    1 <= nums.length <= 105
    nums[i] 不是 0 就是 1
    0 <= k <= nums.length
"""
from collections import defaultdict


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = left = 0
        cnt_0 = 0

        for right, n in enumerate(nums):
            if n == 0:
                cnt_0 += 1

            while cnt_0 > k:
                if nums[left] == 0:
                    cnt_0 -= 1
                left += 1

            ans = max(ans, right - left + 1)

        print(ans)
        return ans


if __name__ == '__main__':
    obj = Solution()
    obj.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2)  # 6
    obj.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3)  # 10
