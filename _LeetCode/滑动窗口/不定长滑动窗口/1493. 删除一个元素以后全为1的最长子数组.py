""" 中等
1493. 删掉一个元素以后全为 1 的最长子数组

给你一个二进制数组 nums，你需要从中删除一个元素。
请你返回删除操作后，数组中仅包含 1 的 最长非空子数组 的长度。如果不存在这样的 子数组，请返回 0。

示例 1：
输入：nums = [1,1,0,1]
输出：3
解释：删除下标为 2 的元素后，得到 [1,1,1]，其中包含 3 个值为 1 的元素。

示例 2：
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删除下标为 4 的元素后，得到 [0,1,1,1,1,1,0,1]，其中仅包含 1 的最长子数组为 [1,1,1,1,1]。

示例 3：
输入：nums = [1,1,1]
输出：2
解释：你必须删除一个元素。

提示：
    1 <= nums.length <= 105
    nums[i] 的值为 0 或 1。
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        res = left = 0

        cnt0 = 0  # 0的个数，维护子数组窗口内最多一个0
        for right, c in enumerate(nums):
            if c == 0:
                cnt0 += 1
            # 窗口内0超过1个，移动左边界收缩窗口
            while cnt0 > 1:
                if nums[left] == 0:
                    cnt0 -= 1
                left += 1

            # 核心改动：窗口长度 - 1（删掉那一个0；全1窗口时，代表要删一个1）
            window_len = right - left + 1
            res = max(res, window_len - 1)
        print(res)
        return res


if __name__ == '__main__':
    obj = Solution()
    obj.longestSubarray([1, 1, 0, 1])  # 3
    obj.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])  # 5
    obj.longestSubarray([1, 1, 1])  # 2
