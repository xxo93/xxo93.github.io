# -*- coding: utf-8 -*-
""" 中等
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
1.路径途经的所有单元格都的值都是 0 。
2.路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

输入：grid = [[0,1],[1,0]]
输出：2

输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4

示例 3：
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1

提示：
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1
"""
import copy
from collections import deque
from math import inf
from typing import List


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """ 基本常规思路 """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0)])     #
        visited[0][0] = True
        step = 1  # 初始步数为1（包含起点）

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return step
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 边界条件处理
                    if (0 <= nx < n and 0 <= ny < n     # 坐标在矩阵内
                    ) and (not visited[nx][ny]          # 没有被访问， False
                    ) and (grid[nx][ny] == 0):          # 值为0的点的坐标，需要添加到访问队列中
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            step += 1
        return -1

    def shortestPathBinaryMatrix_2(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # 起点和终点任意为 1 则不存在满足条件的路径
        if grid[0][0] or grid[row - 1][col - 1]:
            return -1
        # 初始化队列 [x, y, dis]
        visited = {(0, 0)}
        q = deque([(0, 0, 1)])
        # 定义8个方向
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
        while q:
            x, y, dis = q.popleft()
            # 遍历到终点坐标，输出 dis
            if (x, y) == (row - 1, col - 1):
                return dis
            for x_new, y_new in [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y),
                                 (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]:
                if 0 <= x_new < row and 0 <= y_new < col and grid[x_new][y_new] == 0 \
                        and ((x_new, y_new) not in q) and ((x_new, y_new) not in visited):
                    # print('--e------->', (x_new, y_new, dis + 1))
                    q.append((x_new, y_new, dis + 1))
                # # 添加访问过的坐标点
                visited.add((x_new, y_new))
        return -1

    def shortestPathBinaryMatrix_0kb(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1

        queue = [(0, 0, 1)]
        while queue:
            i, j, cnt = queue.pop(0)
            # “坐标超出边界”或“当前坐标值为1”则跳出循环不处理，
            if i < 0 or i > n or j < 0 or j > n or grid[i][j] == 1:
                continue

            # 坐标遍历到终点返回
            if i == n and j == n:
                return cnt

            # 将当前坐标置为1，标记该坐标点已经访问过
            grid[i][j] = 1
            # 遍历当前坐标点的8个方向，
            for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)]:
                queue.append((x, y, cnt + 1))

        return -1

    # BFS耗时短
    def shortestPathBinaryMatrix_耗时短(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 起点和终点为1，则不存在符合条件的路径
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        # 初始化队列 [x, y, dis]
        q = [(0, 0, 1)]
        # 这里直接将grid进行修改，替换了visited集合
        grid[0][0] = 1
        # 遍历队列坐标
        for x, y, dis in q:
            # 遍历到终点坐标，输出 dis
            if x == n - 1 and y == n - 1:
                return dis
            # 遍历8个方向
            for x_new, y_new in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y),
                                 (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)):
                # “满足边界内”and“满足坐标点为0”，则将坐标点添加至队列
                if 0 <= x_new < n and 0 <= y_new < n and not grid[x_new][y_new]:
                    # 将访问过的坐标置为1
                    grid[x_new][y_new] = 1
                    q.append((x_new, y_new, dis + 1))
        return -1

    # 动态规划
    def shortestPathBinaryMatrix_DP(self, grid: List[List[int]]) -> int:
        # 逻辑是 dp[i][j] = arround_min(i,j) + 1
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, 1, -1, -1, 0, 1]
        dist = 0
        N = len(grid)

        # 边界条件
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        if N == 1: return 1
        # 将不可走路径设为inf
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    grid[i][j] = inf
                else:
                    grid[i][j] = 'stop'
        grid[0][0] = 1

        # 定义一个arround_min函数
        def arround_min(i, j):
            _min = inf
            for k in range(8):
                x, y = i + dx[k], j + dy[k]
                if (0 <= x < N and 0 <= y < N and grid[x][y] != 'stop'):
                    _min = min(_min, grid[x][y])
            return _min

        # 这里必须深拷贝，因为是二维数组
        gridnew = copy.deepcopy(grid)

        while (True):
            # 终止条件
            if grid[-1][-1] != inf:
                return grid[-1][-1]

            # 循环
            for j in range(N):
                for i in range(N):
                    if i == 0 and j == 0:
                        continue
                    if grid[i][j] != 'stop':
                        grid[i][j] = arround_min(i, j) + 1

            # 判断grid是否还有变化，若没有则证明无解
            if gridnew == grid:
                return -1
            gridnew = copy.deepcopy(grid)


if __name__ == '__main__':
    o = Solution()
    # print(o.shortestPathBinaryMatrix([
    #     [0, 1],
    #     [1, 0],
    # ]))
    # print(o.shortestPathBinaryMatrix([
    #     [0, 0, 0],
    #     [1, 1, 0],
    #     [1, 1, 0],
    # ]))
    print(o.shortestPathBinaryMatrix([
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]))
    print(o.shortestPathBinaryMatrix_耗时短([
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]))
