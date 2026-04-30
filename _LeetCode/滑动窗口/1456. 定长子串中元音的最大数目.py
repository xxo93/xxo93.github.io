# -*- coding: utf-8 -*-
"""
给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。

示例 1：
输入：s = "baciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。

示例 2：
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。

示例 3：
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

示例 4：
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。

示例 5：
输入：s = "tryhard", k = 4
输出：1
"""
from collections import Counter


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_set = 'aeiou'
        cnt = sum(1 for i in range(k) if s[i] in s_set)

        res = cnt
        l, r = 0, k - 1
        while r < len(s) - 1:
            l += 1
            r += 1
            cnt += -int(s[l - 1] in s_set and s[r] not in s_set) or int(s[l - 1] not in s_set and s[r] in s_set)
            res = max(res, cnt)
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxVowels('ab', 3))  #
    # print(obj.maxVowels('abciiidef', 3))  # 3
    # print(obj.maxVowels('aeiou', 2))  # 2
    # print(obj.maxVowels('leetcode', 3))  # 2
    # print(obj.maxVowels('rhythms', 4))  # 0
    # print(obj.maxVowels('tryhard', 4))  # 1
    # print(obj.maxVowels('novowels', 1))  # 1
