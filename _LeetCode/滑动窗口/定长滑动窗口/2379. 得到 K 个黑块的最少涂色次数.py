# -*- coding: utf-8 -*-
""" 简单
2379. 得到 K 个黑块的最少涂色次数
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。
字符 'W' 和 'B' 分别表示白色和黑色。
给你一个整数 k ，表示想要 连续 黑色块的数目。
每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

示例 1：
输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。

示例 2：
输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。

提示：
n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """ 固定窗口：把‘W’变成‘B’，统计‘W’的数量 """
        n = len(blocks)

        # 先确定第一个位置的初始值
        c = blocks[0: k].count('W')  # 初始值
        res = c
        # 从第二个位置（索引为1的位置）开始滑动。起始位置：1；终止位置: n - k + 1
        for i in range(1, n - k + 1):
            if blocks[i - 1] == 'B' and blocks[i + k - 1] == 'W':
                c += 1
            elif blocks[i - 1] == 'W' and blocks[i + k - 1] == 'B':
                c -= 1
            res = min(res, c)
        print(res)
        return res


if __name__ == '__main__':
    obj = Solution()
    obj.minimumRecolors(blocks='WBBWWBBWBW', k=7)  # 3
    obj.minimumRecolors(blocks='WBWBBBW', k=3)  # 0
    obj.minimumRecolors(blocks='WWBBBWBBBBBWWBWWWB', k=16)  # 6

""" i=2, i+k-1 = 2+16-1= 17
WW BBBWBBBBBWWBWWWB
"""
