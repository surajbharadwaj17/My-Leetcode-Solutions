#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            self.map.pop(val)
            return True

    def getRandom(self) -> int:
        import random
        return random.choice(list(self.map))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

