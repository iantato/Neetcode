'''

--- Neetcode 150 ---
https://neetcode.io/problems/anagram-groups

'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        storage = dict({})

        for word in strs:
            data = ''.join(sorted(word))
            if data not in storage:
                storage[data] = [word]
            else:
                storage.get(data).append(word)

        return [i for i in storage.values()]
