class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for x in nums:
            if x in l:
                return True
            l.append(x)
        return False
        
        