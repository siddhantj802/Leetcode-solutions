class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        flag = False
        dict = {}

        for i , num in enumerate(nums):
            if num in dict and abs(i-dict[num]) <= k:
                flag = True
            dict[num] = i

        return flag
