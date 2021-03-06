#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (63.18%)
# Likes:    3958
# Dislikes: 133
# Total Accepted:    503K
# Total Submissions: 791.7K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # DFS solution
        ret = []
        self.dfs(range(1,n+1), [], k, ret)
        return ret

    def dfs(self, nums, path, k, ret):
        if len(path) == k:
            ret.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], k, ret)

        
# @lc code=end

