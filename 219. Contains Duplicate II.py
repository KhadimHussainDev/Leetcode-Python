class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the latest index of each number
        num_to_index = {}

        for idx, num in enumerate(nums):
            if num not in num_to_index:
                num_to_index[num] = idx
            else:
                # Check if the difference in indices is less than or equal to k
                if abs(num_to_index[num] - idx) <= k:
                    return True
                num_to_index[num] = idx

        return False

## Solution 2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # A set to keep track of the unique numbers seen within the window of size k
        unique_nums = set()

        for i, num in enumerate(nums):
            if num in unique_nums:
                return True  # Found a duplicate within the window
            unique_nums.add(num)  # Add the current number to the set

            # Maintain the window size by removing the element outside the window
            if len(unique_nums) > k:
                unique_nums.remove(nums[i - k])

        return False  # No duplicates found within the window
