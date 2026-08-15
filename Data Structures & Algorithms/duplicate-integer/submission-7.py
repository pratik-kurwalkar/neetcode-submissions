class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = True if len(set(nums)) != len(nums) else False
        return result