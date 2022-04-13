#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (43.38%)
# Likes:    1519
# Dislikes: 156
# Total Accepted:    137.3K
# Total Submissions: 316.3K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# 
# Example 2:
# 
# 
# Input: nums = [5], k = 1
# Output: 5.00000
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        import math
        
        # n = len(nums)
        # left, right = 0, k-1
        # max_avg, cur_sum = -math.inf, 0
        # while right <= n-1:
        #     cur_sum = sum(nums[left:right+1])

        #     avg = cur_sum/k

        #     max_avg = max(max_avg, avg)

        #     left += 1
        #     right += 1

        # return max_avg

        n = len(nums)
        cur_sum = 0
        avg = -math.inf

        # For i > k, start sliding the window 

        for i in range(n):
            cur_sum += nums[i]

            if i > k-1:
                cur_sum -= nums[i-k]
            if i >= k-1:
                avg = max(avg, cur_sum/k)

        return avg

# @lc code=end

