"""
Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""



class Solution:
    def combinationSum(self, nums, target):

        import itertools

        cnt = 0
        for r in range(target+1) :

            for l in itertools.product(nums, repeat = r):
                if sum(l) == target:
                    cnt += 1

        return cnt


soln = Solution()
nums = [1,2,3]
target = 4

print(soln.combinationSum(nums, target))