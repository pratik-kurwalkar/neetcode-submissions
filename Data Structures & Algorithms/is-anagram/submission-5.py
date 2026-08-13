class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1
        for y in t:
            if y not in count:
                return False
            count[y] -= 1
            if count[y] == 0:
                del count[y]
        return not count