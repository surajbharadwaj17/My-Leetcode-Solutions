"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):

        m,n = len(text1), len(text2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):

                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]


soln = Solution()
text1 = 'abcde'
text2 = 'ace'

print(soln.longestCommonSubsequence(text1,text2))