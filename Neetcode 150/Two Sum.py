'''

--- Neetcode 150 ---

Two Sum
https://neetcode.io/problems/two-integer-sum

'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]