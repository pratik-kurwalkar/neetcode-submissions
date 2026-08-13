class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for x in nums:
            if x in map.keys():
                return True
            else:
                map[x] = 1
        return False