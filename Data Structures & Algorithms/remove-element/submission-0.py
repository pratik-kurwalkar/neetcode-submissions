class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for x in range(len(nums)):
            if nums[x] == val:
                count += 1
        for x in range(count):
            nums.remove(val)
        valid = len(nums)
        # for x in range(count):
        #     nums.append('_')
        return valid
        