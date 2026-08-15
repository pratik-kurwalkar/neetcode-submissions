class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for x in range(len(strs[0])):
            for y in range(1, len(strs)):
                try:
                    if strs[0][x] != strs[y][x]:
                        return prefix
                except IndexError:
                        return prefix
            prefix += strs[0][x]
        return prefix

