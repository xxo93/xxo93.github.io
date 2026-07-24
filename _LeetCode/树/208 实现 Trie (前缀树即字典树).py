# -*- coding: utf-8 -*-
"""
208. 实现 Trie (前缀树/字典树)（中等）
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startswith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例：
输入
["Trie", "insert", "search", "search", "startswith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]
解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startswith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

提示：
1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startswith 调用次数 总计 不超过 3 * 104 次
"""
from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    """
    # cat 
    c, False
    a, False
    t, True 
    """

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current is None:
                return False
        return current.isword

    def startswith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current is None:
                return False
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')

    operate_list = ["Trie", "insert", "search", "search", "startswith", "insert", "search"]
    word_list = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    for _op, _wd in tuple(zip(operate_list, word_list)):
        print(f'_op={_op}; _wd={_wd}')
        if not _wd:
            obj = Trie()
        else:
            operate = getattr(obj, _op)
            print(operate(_wd[0]))
