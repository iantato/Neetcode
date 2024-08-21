'''

--- Neetcode 150 ---

Longest Consecutive Sequence
https://neetcode.io/problems/longest-consecutive-sequence

'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sequence = set(nums)
        longest = 0

        for n in sequence:
            if (n - 1) not in sequence:
                length = 1
                while (n + length) in sequence:
                    length += 1
                longest = max(length, longest)
        return longest


x = Solution()
x.longestConsecutive([2,20,4,10,3,4,5])