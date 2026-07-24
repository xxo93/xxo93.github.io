# -*- coding: utf-8 -*-
"""
@auth: 30017121
@date: 2023/2/9 11:25
@desc: 
"""


# 建立字典树
def create_trie(words) -> dict:
    """
    :param words: 单词集
    :return: 返回字典构建的字典树
    """
    trie = {}
    for word in words:
        t = trie  # 请把这个t理解为指针，这个指针除了用来移动外，也用来建立新的字典。
        for w in word:  # cat  {'c': {'a': {'t': {'#': 'cat'}}}
            if w not in t:
                t[w] = {}  # 若没有，为下一个字母建立一个新的字典
            t = t[w]  # 进入下一层
        t['#'] = word  # 句尾结束符
    print(trie)
    return trie


# 查询
def search(char, trie) -> bool:
    """
    :param char: 带查找的词语
    :param trie: 字典查询树
    :return:
    """
    t = trie
    for c in char:
        if c in t:  # 如果我们在本层发现了这个字母，那么，我们进入下一层
            t = t[c]  # 关键点依然是把t理解成指针。
        else:
            return False
    return '#' in t  # 当所有字母都检查完毕的时候，我们需要确定，这个被查询的序列到底是不是一个完整的单词


def startswith(char, trie) -> bool:
    """
    :param char: 带查找的词语
    :param trie: 字典查询树
    :return:
    """
    t = trie
    for c in char:
        if c in t:
            t = t[c]  # 如果有的话进入下一层
        else:
            return False
    return True


def return_startswith(char, trie):
    """ 返回以某个前缀的词
    :param char:
    :param trie:
    :return:
    """
    t = trie
    # 找到字符串的最后一个位置节点
    for c in char:
        if c in t:
            t = t[c]  # 如果有的话进入下一层

    def loop(item: dict, s_list: list):
        if '#' in item.keys():
            s_list.append(item.get('#'))
        else:
            for k, v_dict in item.items():
                loop(v_dict, s_list)
        return s_list

    # 递归获取共同前缀的词语
    words_list = loop(t, [])

    return words_list


if __name__ == '__main__':
    words = ['category', 'tree', 'cat', 'trace', 'top']
    # 构建字典树
    trie_words = create_trie(words)
    # 查找字符
    # print(search('cat', trie_words))
    # print(startswith('tr', trie_words))
    print(return_startswith('tr', trie_words))

"""
['', '' ]
'i am a cat' 
'i am a ***' 
c - a - t(*) - e - g(*) - o - r -y(*)
t - r - e ..
    |
    a - .. 
"""
