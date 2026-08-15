class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            hashmap[nums[x]] = x
        for x in range(len(nums)):
            index = hashmap.get(target - nums[x])
            if index and index != x:
                return [x, index]


