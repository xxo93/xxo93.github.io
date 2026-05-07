# -*- coding: utf-8 -*-
""" 字符串 ok
6. Z 字形变换（中等）
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

提示：
1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 边界情况：只有一行或行数 ≥ 字符串长度，无需变换
        if numRows == 1 or numRows >= len(s):
            return s

        # 创建 numRows 个空字符串，每行一个"篮子"
        rows = [''] * numRows
        cur_row = 0
        direction = 1  # 1 = 向下, -1 = 向上

        # 遍历每个字符，按 Z 字形路径放入对应行
        for c in s:
            rows[cur_row] += c

            # 到达顶部或底部时调头
            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1

            cur_row += direction

        # 拼接所有行
        return ''.join(rows)


if __name__ == '__main__':
    obj = Solution()

    print(obj.convert('PAYPALISHIRING', 3))
    print(obj.convert('PAYPALISHIRING', 4))
    # print(obj.convert('A', 1))
    # print(obj.convert('ABCDEF', 2))
