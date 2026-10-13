# -*- coding: utf-8 -*-
""" 简单，不定长滑动窗口(双指针) + 哈希计数
3090. 每个字符最多出现两次的最长子字符串

给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。

示例 1：
输入： s = "bcbbbcba"
输出： 4
解释：
以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"（取末尾的 "bcba"）。

示例 2：
输入： s = "aaaa"
输出： 2
解释：
以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"（取任意 "aa"）。

提示：
    2 <= s.length <= 100
    s 仅由小写英文字母组成。
"""
from collections import defaultdict, Counter


class Solution:

    def maximumLengthSubstring(self, s: str) -> int:
        """标准解法：不定长滑动窗口 + 哈希计数，左指针只前进不回退，O(n)。

        对应「求最长」模板：窗口不合法（某字符出现 3 次）时收缩左边界。
        """
        ans = left = 0
        cnt = Counter()  # 统计窗口内每个字符的出现次数

        # 通过遍历方式扩展右边界
        for right, c in enumerate(s):
            cnt[c] += 1  # 右边界移入：先把 c 计入窗口（此刻窗口可能短暂非法）

            # 收缩左边，直至满足条件（c 的次数降回 2）
            while cnt[c] > 2:
                cnt[s[left]] -= 1  # 左边界移出：左端字符计数减 1
                left += 1  # 收缩左边界，左指针只增不减

            # 满足条件，计算结果（必须在收缩完成之后更新）
            ans = max(ans, right - left + 1)

        return ans

    def maximumLengthSubstring_2(self, s: str) -> int:
        """原解法：窗口重置版（超标后左指针前移一格，窗口从新起点重建）。

        结果正确，但每次撞上限都把计数字典清空重建、右指针跟着回退重扫，
        最坏情况退化为 O(n^2)（例如长串中反复出现第 3 个相同字符）。
        保留作对照，推荐使用上面的 maximumLengthSubstring。
        """
        n = len(s)
        if n <= 1:
            return n
        count = 0
        p1, p2 = 0, 1  # p1=左指针，p2=右指针
        d = defaultdict(int)
        d[s[p1]] = 1
        while p2 < n:
            if s[p2] not in d or d[s[p2]] <= 1:
                # 未超上限：右指针扩张窗口
                d[s[p2]] += 1
                p2 += 1
                count = max(count, p2 - p1)
            else:
                # 已达上限：左指针右移一格，右指针跟着重置，窗口整体重建
                d[s[p1]] -= 1
                p1 += 1
                p2 = p1 + 1
                d = defaultdict(int)
                d[s[p1]] = 1

        return count


if __name__ == '__main__':
    s = Solution()

    print(s.maximumLengthSubstring("bcbbbcba"))  # 4
    print(s.maximumLengthSubstring("aaaa"))      # 2
    print(s.maximumLengthSubstring("aabbaa"))    # 4
    print(s.maximumLengthSubstring("abcabc"))    # 6
    print(s.maximumLengthSubstring(""))          # 0

    # 原解法对照，结果应一致
    # print(s.maximumLengthSubstring_2("bcbbbcba"))  # 4
    # print(s.maximumLengthSubstring_2("aaaa"))      # 2
