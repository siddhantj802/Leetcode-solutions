class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       left = 0
       maxCount = 0
       zeroCounter = 0

       for right in range(len(nums)):
           if nums[right] == 0:
               zeroCounter += 1

           while zeroCounter > k:
                if nums[left] == 0:
                    zeroCounter -= 1
                left += 1

           maxCount = max(maxCount , right-left+1)

       return maxCount

        
