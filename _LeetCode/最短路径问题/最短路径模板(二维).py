# -*- coding: utf-8 -*-
"""
【二维】网格中内有不同的数字，数字表示某种特性，求解从起点到终点所需的最小值。
该类问题常用"广度优先搜索"方法 BFS，优化可采用双向 BFS，另外也可以尝试使用 DP。

定义队列；
定义备忘录，用于记录已经访问的位置；

将起始位置加入到队列中，同时更新备忘录。

while (队列不为空){
    获取当前队列中的元素个数。
    判断是否到达终点位置。

    for (元素个数){
        取出一个位置节点。
        判断是否到达终点位置。
        获取它对应的下一个所有的节点。
        条件判断，过滤掉不符合条件的位置。
        新位置重新加入队列。
    }
}
"""

from collections import deque


def bfs(nums):
    row = len(nums)
    col = len(nums[0])
    visited = {(0, 0)}  # 记录[已访问的坐标]
    q = [(0, 0, 1)]  # [(x, y, step)]: x, y 表示[已访问的方格的坐标]，step(dis) 表示到达当前方格所需要的操作步数，起步为 1
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 搜索的方向
    for x, y, dis in q:
        if x == row - 1 and y == col - 1:
            # 达到终点时返回dis
            return dis
        # 遍历4个方向
        for i, j in direction:
            x_new, y_new = x + i, y + j
            # 判断满足条件时，将满足的方格加入到 visited 和 q 中，同时dis需要进行加一操作
            if (0 <= x_new < row) and (0 <= y_new < col) and nums[x_new][y_new] == 0:
                visited.add((x_new, y_new))
                q.append((x_new, y_new, dis + 1))
    return -1  # 以上for循环没有输出，说明得不到答案，执行到这里返回-1


def bfs2(nums):
    row = len(nums)
    col = len(nums[0])
    visited = {(0, 0)}  # 记录已访问的坐标
    q = deque([(0, 0, 1)])  # [(x, y, step)]: x, y 表示[已访问的方格的坐标]，step(dis) 表示到达当前方格所需要的操作步数，起步为 1
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y, dis = q.popleft()
        # 直到遍历到最后一个位置，输出距离 dis
        if x == row - 1 and y == col - 1:
            return dis
        # 不是终点，不断搜索4个方向
        for i, j in direction:
            x_new = x + i
            y_new = y + j
            if 0 <= x_new < row and 0 <= y_new < col and nums[x_new][y_new] == 0:
                # 添加访问过的坐标
                visited.add((x_new, y_new))
                # 访问过的坐标不添加队列（不走回头路）
                if (x_new, y_new, dis + 1) not in q:
                    q.append((x_new, y_new, dis + 1))
    return -1


if __name__ == '__main__':
    print(bfs([
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]))
    print(bfs2([
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]))
