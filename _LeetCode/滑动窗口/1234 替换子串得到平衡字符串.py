# -*- coding: utf-8 -*-
"""
@auth: 30017121
@date: 2023/2/13 9:49
@desc: 中等，滑动窗口
1234. 替换子串得到平衡字符串
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
请返回待替换子串的最小可能长度。
如果原字符串自身就是一个平衡字符串，则返回 0。


示例 1：
输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。

示例 2：
输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。

示例 3：
输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。

示例 4：
输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。

示例 5：
输入：s = "WQWQQRQW"
输出：3


"""
from collections import Counter
from math import inf


class Solution:
    def balancedString(self, s: str) -> int:
        count_dict, m = Counter(s), len(s) // 4

        if all(count_dict[x] == m for x in "QWER"):  # 已经符合要求啦
            return 0

        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            # 维护子串外平衡
            count_dict[c] -= 1
            while all(count_dict[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                count_dict[s[left]] += 1  # 将左端点的字符计数添加回去
                left += 1  # 缩小子串
        return ans


if __name__ == '__main__':
    obj = Solution()

    # print(obj.balancedString("QWER"))
    # print(obj.balancedString("QQWE"))
    # print(obj.balancedString("QQQW"))
    # print(obj.balancedString("QQQQ"))
    # print(obj.balancedString("WQWQQRQW"))
    print(obj.balancedString("WQQQRRQRRREW"))

    # print(obj.balancedString("WWEQERQWQWWRWWERQWEQ"))
    # print(obj.balancedString_2("WWEQERQWQWWRWWERQWEQ"))
