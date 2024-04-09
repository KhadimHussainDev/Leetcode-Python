#Solution 1 (Not clean)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1 
        def binarySearch(left , right):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        while left <= right :
            if nums[left] < nums[right]:
                return binarySearch(left , right)
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if (nums[mid] > nums[left] and nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and (target >= nums[left] or target < nums[mid])):
                right = mid - 1
            else:
                left = mid + 1        
        return -1

#Solution 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1  # Calculate the middle index

            if nums[mid] == target:
                return mid  # Return the index if target is found

            if nums[mid] >= nums[left]:
                # Check if the left half is sorted and target is within this range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Adjust right boundary
                else:
                    left = mid + 1  # Adjust left boundary
            else:
                # Check if the right half is sorted and target is within this range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Adjust left boundary
                else:
                    right = mid - 1  # Adjust right boundary

        return -1  # Return -1 if target is not found
