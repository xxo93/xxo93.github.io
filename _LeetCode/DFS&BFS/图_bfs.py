"""
实现BFS的图
"""
from collections import deque

# 创建一个字典，用于存储图。字典相当于映射关系，通过键值对进行读取。
graph_data = {
    "A": ["B", "C", "E"],
    "B": ["A", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["A", "C", "D", "F", "H"],
    "F": ["D", "E"]
}


# 开始BFS遍历
def bfs(graph, s):
    """
    :param graph: 图数据
    :param s: 图的起点
    :return:
    """
    # 创建一个数组作为队列，用于存储未访问过的点，首先放入起点
    queue = deque()
    queue.append(s)

    # 创建一个集合，用于存放已读入的点
    visited = set()
    visited.add(s)

    # 路径还原，把访问的点和它前一个点对应起来，形成一个键值对，利用它来完成最短路径的输出
    parent = {s: None}

    # 循环读queue
    while queue:
        # 通过queue.popleft()读取队列队首,即每个点
        point = queue.popleft()
        # 读取每个点相邻的点
        nodes = graph.get(point, [])

        # 判重：循环判断相邻的点是否读过
        for w in nodes:
            if w not in visited:
                queue.append(w)  # 将未访问的点加入队列，循环处理队列元素
                visited.add(w)  # 将未访问的点加入已访问的集合
                parent[w] = point  # 记录最先访问到该节点时的父节点

        # 输出遍历节点
        print(point, end=' ')

    return parent


parent_dict = bfs(graph_data, "A")

print('\n------------------')
# 输出你想要的到最短路径
# 设v为终点
v = 'F'
# 循环查找v
while v:
    print(v, end=' ')
    v = parent_dict[v]

