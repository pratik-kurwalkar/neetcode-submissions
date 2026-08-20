class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            print("start:", start, "end:", end)
            mid = (start + end) // 2
            print("mid:", mid)
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[start]:
                # assume correctly sorted till mid
                if target < nums[mid] and target >= nums[start]:
                    # look at the left side (correctly sorted)
                    end = mid - 1
                else:
                    # llok at the right side (rotated)
                    start = mid + 1
            else:
                # roted piv before mid
                if target > nums[mid]:
                    if target > nums[end]:
                        end = mid - 1
                        
                    else:
                        start = mid + 1
                    
                else:
                    #look at the left side 
                    
                    end = mid - 1
        return -1 