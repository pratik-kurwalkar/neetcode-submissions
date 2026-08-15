class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for x in strs:
            key = [0] * 30
            for y in x:
                key[ord(y)-95] += 1
            words = keys.get(tuple(key), [])
            words.append(x)
            keys[tuple(key)] = words
        return list(keys.values())
