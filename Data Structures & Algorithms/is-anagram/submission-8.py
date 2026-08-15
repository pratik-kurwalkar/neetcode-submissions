class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for x in s:
            if dict_s.get(x) == None:
                dict_s[x] = 1
            else:
                dict_s[x] += 1
        for y in t:
            if dict_s.get(y) == None or dict_s.get(y) == 0:
                return False
            else:
                dict_s[y] -= 1
        if list(set(dict_s.values())) == [0]:
            return True
        else:
            return False