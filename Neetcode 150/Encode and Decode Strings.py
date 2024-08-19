'''

--- Neetcode 150 ---

Encode and Decode Strings
https://neetcode.io/problems/string-encode-and-decode

'''

class Solution:
    def encode(self, strs: list[str]) -> str:
        if strs == []:
            return '[]'
        return '1#'.join(strs)

    def decode(self, s: str) -> list[str]:
        if s == []:
            return '[]'
        return s.split("1#")