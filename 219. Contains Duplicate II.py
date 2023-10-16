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
