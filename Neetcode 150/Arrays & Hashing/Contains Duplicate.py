'''

--- Neetcode 150 ---

Duplicate Integer
https://neetcode.io/problems/duplicate-integer

'''

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in set(nums):
            if nums.count(i) > 1:
                return True
        return False