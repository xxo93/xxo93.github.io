# -*- coding: utf-8 -*-
""" 中等
1343. 大小为 K 且平均值大于等于阈值的子数组数目
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

示例 1：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

示例 2：
输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。

提示：
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^4
1 <= k <= arr.length
0 <= threshold <= 10^4
"""
from typing import List


class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = k * threshold
        arr_s_sum = sum(arr[:k])
        cnt = 0
        if len(arr) == k and arr_s_sum >= s:
            cnt += 1
            return cnt

        diff = arr_s_sum - s  # 第一个差值
        if diff >= 0:
            cnt += 1

        for i in range(1, len(arr) - k + 1):
            diff = diff - arr[i - 1] + arr[i + k - 1]
            if diff >= 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    obj = Solution()
    print(obj.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))  # 3
    print(obj.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))  # 6
    print(obj.numOfSubarrays([1, 1, 1, 1, 1], k=1, threshold=0))  # 5
