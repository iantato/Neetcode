'''

--- Neetcode 150 ---

Top K Elements in List
https://neetcode.io/problems/top-k-elements-in-list

'''
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [i for (i, k) in Counter(nums).most_common(k)]