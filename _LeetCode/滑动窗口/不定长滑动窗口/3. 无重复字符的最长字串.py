# -*- coding: utf-8 -*-
""" 中等，不定长滑动窗口(双指针) + 哈希集合
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：
    0 <= s.length <= 105
    s 由英文字母、数字、符号和空格组成
"""
from collections import Counter


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = Counter()  # 统计数量

        # 通过遍历方式扩展右边界
        for right, c in enumerate(s):
            cnt[right] += 1

            # 收缩左边，直至满足条件
            while cnt[right] > 1:
                cnt[s[left]] -= 1
                left += 1
            # 满足条件后，计算最大值
            ans = max(ans, right - left + 1)

        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """标准解法：不定长滑动窗口 + 哈希集合，左指针只前进不回退，O(n)。

        对应「求最长」模板：窗口不合法（出现重复）时收缩左边界。
        """
        window = set()  # 窗口内出现的字符集合
        left = 0  # 左指针：只增不减
        ans = 0

        for right, c in enumerate(s):  # 右指针：每轮无条件右移一格
            # 1. 收缩：新字符 c 与窗口内字符撞车，就把左端字符逐个甩出去
            while c in window:
                window.remove(s[left])  # 移出左端字符
                left += 1  # 左指针右移，缩小窗口

            # 2. 扩张：此时窗口已无重复，放心把 c 放进来
            window.add(c)

            # 3. 更新答案：必须先收缩到合法，再用窗口长度更新
            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.lengthOfLongestSubstring2(s="abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring2(s="bbbbb"))  # 1
    print(s.lengthOfLongestSubstring2(s="pwwkew"))  # 3
    print(s.lengthOfLongestSubstring2(s=""))  # 0
    print(s.lengthOfLongestSubstring2(s="abcbbacbb"))  # 3

    # 原解法对照，结果应一致
    # print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3
    # print(s.lengthOfLongestSubstring(s="bbbbb"))     # 1
    # print(s.lengthOfLongestSubstring(s="pwwkew"))    # 3
    # print(s.lengthOfLongestSubstring(s="abcbbacbb"))  # 3
