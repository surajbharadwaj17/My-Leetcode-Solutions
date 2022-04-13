#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (49.97%)
# Likes:    5516
# Dislikes: 145
# Total Accepted:    198.3K
# Total Submissions: 383.6K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# 
# Write an algorithm to minimize the largest sum among these m subarrays.
# 
# 
# Example 1:
# 
# 
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,4,4], m = 3
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= m <= min(50, nums.length)
# 
# 
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        lo,hi = max(nums), sum(nums)

        while(lo < hi):
            mid = (lo+hi)//2

            total, cnt = 0,1
            for num in nums:
                if num+total <= mid:
                    total += num
                else:
                    
                    total = num
                    cnt += 1
            
            if cnt > m:
                lo = mid +1
            else:
                hi = mid

        return hi
# @lc code=end

