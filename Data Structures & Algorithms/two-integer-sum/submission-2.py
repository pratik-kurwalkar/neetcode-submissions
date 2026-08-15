class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            
        # for x in range(len(nums)):
            diff = target - nums[x]
            if diff in hashmap:
                return [hashmap[diff], x]
            hashmap[nums[x]] = x


