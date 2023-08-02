class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        length = len(nums)

        if length <= k :
            return sum(nums)/k

        windowSum = sum(nums[:k])
        maxSum = windowSum
            

        for i in range(k,length):
            windowSum = windowSum - nums[i-k] + nums[i]
            maxSum = max(maxSum , windowSum)

        return maxSum/k
