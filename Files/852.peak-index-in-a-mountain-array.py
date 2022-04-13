#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (70.93%)
# Likes:    2269
# Dislikes: 1595
# Total Accepted:    336.1K
# Total Submissions: 474.3K
# Testcase Example:  '[0,1,0]'
#
# Let's call an array arr a mountain if the following properties hold:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... arr[i-1] < arr[i] 
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# Given an integer array arr that is guaranteed to be a mountain, return any i
# such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... >
# arr[arr.length - 1].
# 
# 
# Example 1:
# 
# 
# Input: arr = [0,1,0]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: arr = [0,2,1,0]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: arr = [0,10,5,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
# 
# 
# 
# Follow up: Finding the O(n) is straightforward, could you find an O(log(n))
# solution?
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0,len(arr)-1

        while(left <= right):
            mid = (left+right)//2

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid

            if arr[mid] < arr[mid+1] :
                left = mid+1
            else:
                right = mid-1



        
# @lc code=end

