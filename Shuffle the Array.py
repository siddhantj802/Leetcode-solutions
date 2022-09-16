class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xele = 0
        yele = n
        
        anslist = []
        
        while xele < n:
            anslist.append(nums[xele])
            anslist.append(nums[yele])
            xele += 1
            yele += 1
        return anslist
        
