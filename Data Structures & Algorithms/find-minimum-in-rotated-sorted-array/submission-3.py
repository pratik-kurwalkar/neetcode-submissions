class Solution:
    def findMin(self, nums: List[int]) -> int:
        start_index = 0
        end_index = len(nums) - 1
        if nums[start_index] <= nums[end_index]:
            return nums[0]
        while nums[start_index] > nums[end_index]:
            mid_index = start_index + ((end_index - start_index) // 2)
            print("start:", start_index, "end:", end_index, "mid:", mid_index)
            if nums[mid_index] > nums[start_index]:
                start_index = mid_index
            else:
                end_index = mid_index
        return nums[start_index + 1]

        