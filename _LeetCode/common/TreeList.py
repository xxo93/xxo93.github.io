# -*- coding: utf-8 -*-
""" 层序遍历 """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree2List:
    """ 二叉树的遍历（转列表） """

    @classmethod
    def tree2list_sequence(cls, root: TreeNode) -> list:
        """ 层序遍历 """
        if not root:
            return []
        res = [root.val]
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(f'+++ node={node.val}')
            if node.left and (node.left.val is not None):
                queue.append(node.left)
                res.append(node.left.val)
            else:
                res.append(None)
            if node.right and (node.right.val is not None):
                queue.append(node.right)
                res.append(node.right.val)
            else:
                res.append(None)

        return res

    @classmethod
    def tree2list_prior(cls, root: TreeNode) -> list:
        """ 先序遍历 """
        node_list = []

        def loop(node, arr):
            if node:
                # 保留 None 的数据域
                # arr.append(node.val)
                # 不保留 None 的数据域
                if node.val:
                    arr.append(node.val)
                loop(node.left, arr)
                loop(node.right, arr)

        loop(root, node_list)
        return node_list

    @classmethod
    def tree2list_middle(cls, root: TreeNode) -> list:
        """ 中序遍历 """
        node_list = []

        def loop(node, arr):
            if node:
                loop(node.left, arr)

                # 保留 None 的数据域
                # arr.append(node.val)
                # 不保留 None 的数据域
                if node.val:
                    arr.append(node.val)

                loop(node.right, arr)

        loop(root, node_list)
        return node_list

    @classmethod
    def tree2list_post(cls, root: TreeNode) -> list:
        """ 后序遍历 """
        node_list = []

        def loop(node, arr):
            if node:
                loop(node.left, arr)
                loop(node.right, arr)

                # 保留 None 的数据域
                # arr.append(node.val)
                # 不保留 None 的数据域
                if node.val:
                    arr.append(node.val)

        loop(root, node_list)
        return node_list


class List2BinaryTree:
    """ 列表转二叉树 """

    def __init__(self):
        """ 初始化根节点 """
        self.root = TreeNode()

    @classmethod
    def list2tree_sequence(cls, arr: list) -> [TreeNode, None]:
        """ [层序遍历]的列表转二叉树 """
        cls.root = TreeNode()
        if not arr:
            return None

        queue = [cls.root]
        cls.root.val = arr[0]
        i = 1
        while i < len(arr):
            node = queue.pop(0)
            # print(f'node={node.val}')

            node.left = TreeNode()
            node.left.val = arr[i]
            if node.left.val is not None:
                queue.append(node.left)

            node.right = TreeNode()
            node.right.val = arr[i + 1] if (i + 1) < len(arr) else None
            if node.right.val is not None:
                queue.append(node.right)
            i += 2

        return cls.root

    # def list2tree_prior(self, arr: list) -> TreeNode:
    #     """ [先序遍历]的列表转二叉树 """
    #
    #     return TreeNode()
    #
    # def list2tree_middle(self, arr: list) -> TreeNode:
    #     """ [中序遍历]的列表转二叉树 """
    #
    #     return TreeNode()
    #
    # def list2tree_post(self, arr: list) -> TreeNode:
    #     """ [后序遍历]的列表转二叉树 """
    #
    #     return TreeNode()


if __name__ == '__main__':
    array = List2BinaryTree()
    root = array.list2tree_sequence([2, 1, 3, 5, 4, 6, None, 10])

    # 层序遍历
    print(BinaryTree2List().tree2list_sequence(root))
    # 先序遍历
    print(BinaryTree2List().tree2list_prior(root))
    # 中序遍历
    print(BinaryTree2List().tree2list_middle(root))
    # 后序遍历
    print(BinaryTree2List().tree2list_post(root))
