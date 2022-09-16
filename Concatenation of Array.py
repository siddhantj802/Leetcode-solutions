class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_list = [0] * 2*n
        
        for i in range(n):
            ans_list[i] = nums[i]
            ans_list[i+n] = nums[i]
            
        return ans_list
