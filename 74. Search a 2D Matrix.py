#Solution 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search to identify the potential row where the target might be located
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid = (top + bot) >> 1
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        # Perform binary search within the identified row to find the target
        row = mid
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) >> 1
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False