# -*- coding: utf-8 -*-
""" 中等，【字典树/前缀树】，数组，字符串

1233. 删除子文件夹

你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。


示例 1：
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

示例 2：
输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d" 都会被删除，因为它们都是 "/a" 的子文件夹。

示例 3：
输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]
"""
from typing import List


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """ 字典树方法 """

        # 创建字典树
        def create_trie(folder_list: List[List[str]]) -> dict:
            trie = {}
            for folder in folder_list:
                t = trie
                for s in folder:
                    if s not in t:
                        t[s] = {}
                    t = t[s]
                t['#'] = "#"  # 结束符
            return trie

        # 预处理目录集合
        folder_list = [i[1:].split('/') for i in folder]

        trie = create_trie(folder_list)

        res = []
        for folder in folder_list:
            t = trie
            # 处理单个目录
            folder_s = ''
            for s in folder:
                if s in t and '#' not in t[s]:
                    folder_s += '/' + s
                    t = t[s]
                else:
                    folder_s += '/' + s
                    break

            if folder_s not in res:
                res.append(folder_s)

        return res

    def removeSubfolders_sort(self, folder: List[str]) -> List[str]:
        """ 排序方法 """
        folder_list = [i[1:].split('/') for i in folder]
        folder_list.sort()
        res = []
        for _folder in folder_list:
            _dir = ''
            for s in _folder:
                _dir += '/' + s
                if _dir in res:
                    break
            if _dir not in res:
                res.append(_dir)

        return res

    def removeSubfolders_sort2(self, folder: List[str]) -> List[str]:
        """ 排序方法2 """
        folder.sort()
        ans = []
        for f in folder:
            if ans:
                if not f.startswith(ans[-1] + '/'):
                    ans.append(f)
            else:
                ans.append(f)

        return ans


if __name__ == '__main__':
    obj = Solution()

    print(obj.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    print(obj.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
    print(obj.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))

    print(obj.removeSubfolders_sort(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    print(obj.removeSubfolders_sort(["/a", "/a/b/c", "/a/b/d"]))
    print(obj.removeSubfolders_sort(["/a/b/c", "/a/b/ca", "/a/b/d"]))

    print(obj.removeSubfolders_sort2(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    print(obj.removeSubfolders_sort2(["/a", "/a/b/c", "/a/b/d"]))
    print(obj.removeSubfolders_sort2(["/a/b/c", "/a/b/ca", "/a/b/d"]))
