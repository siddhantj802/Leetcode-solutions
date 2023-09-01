class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        summ = sum(arr[:k]) 

        if summ / k >= threshold:
            count += 1

        for i in range(k , len(arr)):
            summ = summ - arr[i-k] + arr[i]
            
            res = summ/k
            
            if res >= threshold:
                count += 1
        return count
                
