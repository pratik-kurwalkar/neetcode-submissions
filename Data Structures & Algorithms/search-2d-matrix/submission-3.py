class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search_row(row, target):
            if len(row) < 1:
                return False
            mid = len(row) // 2
            if target == row[mid]:
                return True
            if target < row[mid]:
                return search_row(row[:mid], target)
            else:
                return search_row(row[mid+1:], target) 

        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][0] and target > matrix[mid][len(matrix[mid]) - 1]:
                start = mid + 1
            else:
                return search_row(matrix[mid], target)
        return False

