#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (47.96%)
# Likes:    6836
# Dislikes: 119
# Total Accepted:    568.8K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

      m_up,m_down = 0, len(matrix)-1
      n_left, n_right = 0, len(matrix[0])-1

      while(m_up < m_down and n_left < n_right):

        m_mid = (m_up+m_down)//2
        n_mid = (n_left+n_right)//2

        print(matrix[m_mid][n_mid])

        if target == matrix[m_mid][n_mid]:
          return True

        if target < matrix[m_mid][n_mid]:
          m_down = m_mid-1
          n_right = n_mid-1

        else:
          m_up = m_mid+1
          n_left = n_mid+1

        

      return False
      
        
# @lc code=end

