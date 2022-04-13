"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        hmap = defaultdict(list)

        for word in strs:
            count = [0]*26
            
            for char in word:
                count[ord(char) - ord('a')] += 1

            hmap[tuple(count)].append(word)

        return hmap.values()

soln = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

print(soln.groupAnagrams(strs))