class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if abs(nums[i] - nums[j]) == k :
                    count += 1
                j += 1
        return count
