def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict  = {}
    
    for i , x in enumerate(nums):
        diff = target - x
        
        if diff in nums_dict:
            return [i , nums_dict[diff]]
        else:
            nums_dict[x] = i
