class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][0] and target > matrix[mid][len(matrix[mid]) - 1]:
                start = mid + 1
            else:
                row = matrix[mid]
                start = 0
                end = len(row) - 1
                while start <= end:
                    mid = start + ((end - start) // 2)
                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                return False
        return False

