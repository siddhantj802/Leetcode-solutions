class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       length = len(nums)
       aPointer = 0
       bPointer = 1

       if length < 2:
           return nums

       while  bPointer < length:

           if nums[aPointer] == 0 and nums[bPointer] != 0:
               temp = nums[aPointer]
               
            
               nums[aPointer] = nums[bPointer]
               nums[bPointer] = temp

               aPointer += 1
               bPointer += 1

           elif nums[aPointer] == 0 and nums[bPointer] == 0:
               bPointer += 1

           else:
               aPointer += 1
               bPointer += 1
