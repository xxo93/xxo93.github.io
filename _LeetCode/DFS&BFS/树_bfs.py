"""
实现BFS的树
"""
from collections import deque


# 定义一个树的节点
class TreeNode:
    def __init__(self, x):
        self.val = x  # 值
        self.left = None  # 左节点
        self.right = None  # 右节点


def level_order_tree(root):
    if not root:  # 一个树只有根节点，返回空值
        return root
    queue = deque()
    result = []
    queue.append(root)  # 将根节点入队
    while queue:
        node = queue.popleft()  # 取队列队首
        result.append(node.val)
        # 判断左右子树
        if node.left:  # 添加左子树的孩子(左子节点)到队列
            queue.append(node.left)
        if node.right:  # 添加右子树的孩子(右子节点)到队列
            queue.append(node.right)
    return result


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.right = TreeNode(0)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)

    print(level_order_tree(tree))
