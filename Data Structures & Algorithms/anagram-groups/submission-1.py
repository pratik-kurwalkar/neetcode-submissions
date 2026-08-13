class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for string in strs:
            charList = [0]*26
            for char in string:
                charList[ord(char)-ord('a')] += 1
            key = str(charList)
            if key in anagramMap:
                anagramMap[key].append(string)
            else:
                anagramMap[key] = [string]
        return list(anagramMap.values())