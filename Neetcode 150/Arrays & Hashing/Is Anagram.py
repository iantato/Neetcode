'''

--- Neetcode 150 ---

Valid Anagram
https://neetcode.io/problems/is-anagram

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False