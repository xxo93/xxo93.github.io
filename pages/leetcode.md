---
layout: default
title: LeetCode
---

# 🧠 LeetCode 算法

## 分类
- 动态规划
- BFS / DFS
- 贪心算法

---

## 示例文章

### 题目：最长递增子序列

思路：
- 定义 dp[i]
- 状态转移

```python
def lengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
