"""
====================================
 滑动窗口（Sliding Window）通用模板
====================================

算法思想：
    用「左右双指针」维护一个窗口，通过移动右指针扩窗口、移动左指针缩窗口，
    在窗口满足/不满足条件时更新答案。常用于解决「子数组 / 子串」相关的问题。

分类：
    ① 定长滑动窗口 —— 窗口长度固定为 k，每次右移一步、左移一步（整体平移）。
    ② 不定长滑动窗口 —— 窗口长度可变，根据条件伸缩。
        不定长又可分为：
        a) 求「最长 / 最多」：窗口不合法时收缩左边界。
        b) 求「最短 / 最少」：窗口合法时收缩左边界（尝试找更短）。
        c) 求「方案 / 计数」：在合法区间内统计右端点固定时的合法左端点范围。
"""
from cmath import inf


# =================== ① 定长滑动窗口 ===================
# 适用场景：窗口长度固定为 k，求窗口内的统计量（和、最大值、个数等）。
# 核心套路：
#   1) 先初始化前 k 个元素作为第一个窗口。
#   2) 移动窗口时“先进后出”：加入窗口右侧新元素，移除窗口左侧旧元素。
#   3) 更新答案。


def fixed_window_k_sum(nums, k):
    """
    模板示例：定长窗口的「和」。
    每次窗口右移一步，滑动更新窗口和（O(1) 维护，无需重新累加）。
    """
    if len(nums) < k:
        return -1

    # 1. 先计算第一个窗口的和
    window_sum = sum(nums[:k])
    res = window_sum                    # 维护答案

    # 2. 整体右移窗口（从 i=k 开始，i 是滑动后窗口的最右端下标）
    for i in range(k, len(nums)):
        # 进：把新元素 nums[i] 加入窗口
        window_sum += nums[i]
        # 出：把旧元素 nums[i - k] 移出窗口
        window_sum -= nums[i - k]

        # 3. 更新答案
        res = max(res, window_sum)      # 按题意更新，这里以求最大和为例

    return res


# =================== ② 不定长滑动窗口 ===================

# -------- ②-a 求「最长 / 最多」--------
# 适用场景：寻找满足约束的【最长】子数组/子串长度。
# 核心套路：
#   1) 右指针不断右移【扩窗口】（总是可以无脑扩）。
#   2) 一旦窗口【不满足】题目约束，左指针右移【缩窗口】，直到恢复合法。
#   3) 每个右端位置都合法时，更新「最长」答案。


def longest_valid_subarray(nums):
    """
    模板示例：求满足某约束 condition(窗口) 的最长子数组长度。
    假设 condition 窗口内元素种类/累加和 <= limit 之类。
    """
    n = len(nums)
    left = 0
    ans = 0

    for right in range(n):
        # 扩窗口：把 nums[right] 加入（通常需维护窗口内状态，如计数、求和）
        # add(nums[right])

        # 窗口不合法：缩小左边界直到再次合法
        while left <= right and not condition(left, right):
            # remove(nums[left])   # 撤销左端元素对状态的影响
            left += 1

        # 此时 [left, right] 是合法窗口，更新答案
        ans = max(ans, right - left + 1)

    return ans


# -------- ②-b 求「最短 / 最少」--------
# 适用场景：寻找满足约束的【最短】子数组/子串长度。
# 核心套路：
#   1) 右指针右移【扩窗口】。
#   2) 一旦窗口【满足】题目约束，尝试左指针右移【缩窗口】以找更短的答案。
#   3) 在缩窗口的过程中，每次缩都更新「最短」答案。


def shortest_valid_subarray(nums, target):
    """
    模板示例（LeetCode 209 长度最小的子数组）：
    求累加和 >= target 的最短子数组长度。
    """
    n = len(nums)
    left = 0
    window_sum = 0
    ans = float('inf')                    # 最短需要用无穷大初始化

    for right in range(n):
        # 扩窗口
        window_sum += nums[right]

        # 窗口满足约束（sum >= target）时，收缩左边界找最短
        while window_sum >= target:
            ans = min(ans, right - left + 1)
            # 缩窗口（移出左端元素）
            window_sum -= nums[left]
            left += 1

    return 0 if ans == float('inf') else ans


# -------- ②-c 求「方案 / 计数」（灵活题型）--------
# 适用场景：统计满足约束（如乘积 < k、和 <= limit）的连续子数组个数。
# 核心套路：
#   1) 右指针右移【扩窗口】。
#   2) 窗口【不满足】约束时，左指针右移【缩窗口】。
#   3) 对固定右端点 right，所有以 right 结尾且左端点取 [left, right]
#      的窗口都合法，因此贡献 right - left + 1 个方案，累加入答案。


def count_valid_subarrays(nums, limit):
    """
    模板示例（LeetCode 713 乘积小于 K 的子数组）：
    统计元素乘积 < limit 的连续子数组个数。
    """
    n = len(nums)
    left = 0
    product = 1
    ans = 0

    for right in range(n):
        # 扩窗口
        product *= nums[right]

        # 窗口不满足约束（乘积 >= limit）时，缩窗口
        while product >= limit:
            product //= nums[left]
            left += 1

        # [left, right] 内任一以 right 结尾的子数组都合法，共 right-left+1 个
        ans += right - left + 1

    return ans


"""
========================
 总结：三类模板如何选？
========================
  1. 窗口长度固定为 k   → 用「定长模板」，先进后出（O(1) 滑动更新）。
  2. 窗口不合法才缩   → 求「最长/最多」。
  3. 窗口合法就尝试缩 → 求「最短/最少」。
  4. 合法即计数的题型 → 用公式 right-left+1 累加方案数。

核心技巧：
  · 什么时候扩？      —— 右指针 for 循环天然前进（永远先扩）。
  · 什么时候缩？      —— 破坏条件(最长式) 或 满足条件(最短式) 时左移。
  · 什么时候更新答案？ —— 注意是缩窗口【之前】更新还是【之后】更新。
"""
