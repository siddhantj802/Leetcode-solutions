class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans_list = []
        for i in range (len(nums)) :
            ans_list.append(nums[nums[i]])
        return ans_list
