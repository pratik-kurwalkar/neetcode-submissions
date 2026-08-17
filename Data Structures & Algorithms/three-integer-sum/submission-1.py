class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums = sorted(nums)
        for x in range(len(nums)):
            if x != 0 and nums[x] == nums[x - 1]:
                continue
            l, r = x + 1, len(nums) - 1
            while l < r:
                if nums[x] + nums[l] > -1 * nums[r]:
                    r -= 1
                elif nums[x] + nums[l] < -1 * nums[r]:
                    l += 1
                else:
                    triplet.append([nums[x], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
        return triplet
