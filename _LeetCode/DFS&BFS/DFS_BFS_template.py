from collections import deque


def bfs(start, target):
    """ bfs模板框架
    :param start:
    :param target:
    :return:
    """
    queue = deque()                      # 核心数据结构-队列
    visited = set()                 	 # 记录走过的路径，避免走回头路--使用集合，检索速度更快
    queue.append(start)
    visited.add(start)
    step = 0	                         # 记录扩散的步数
    while queue:
        size = len(queue)          	 	 # 将当前队列中的所有节点向四周扩散
        for i in range(size):
            cur = queue.popleft()
            if cur == target:       	 # 划重点：这里判断是否到达终点
                return step
            for node in cur:        	 # 将cur的相邻节点加入队列
                if node not in visited:  # 否则会出现大量冗余
                    queue.append(node)
                    visited.add(node)
        step += 1                   	 # 划重点：这里更新步数
    return step

