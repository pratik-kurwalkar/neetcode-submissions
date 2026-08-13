class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (2 * len(nums))
        for x in range(len(nums)):
            ans[x] = nums[x]
            ans[len(nums)+x] = nums[x]
        return ans