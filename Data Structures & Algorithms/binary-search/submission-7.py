class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_binary_search(start, end):
            mid = start + ((end - start) // 2)
            if target == nums[mid]:
                return mid
            if start > mid:
                return -1
            if target < nums[mid]:
                return recursive_binary_search(start, mid - 1)
            else:
                return recursive_binary_search(mid + 1, end)
        return recursive_binary_search(0, len(nums) - 1)
        

